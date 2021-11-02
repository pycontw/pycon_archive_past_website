import json
import re
from pathlib import Path
from urllib.parse import unquote, urlparse
from common.dataio import mkdir
from common.scrap import get_soup
from websites import CRAWLERS, BaseCrawler
from websites.utilities import get_asset

import click
from loguru import logger

PYCON_YEAR = "2016"
PYCON_URL = f"https://tw.pycon.org"


def getcssimg(path):
    path = urlparse(path).path
    # get all url like /year/... target, and try to save them all.
    file = "." + path
    with open(file, "rb") as f:
        content = str(f.read())
        all_url = re.findall("/" + PYCON_YEAR + r"[^\s]*", content)
        for url in all_url:
            url = url.replace("\\n", "")
            url = url[0 : url.rfind("\\")]
            url = url[0 : url.rfind("?")]
            if not Path("." + url).exists():
                get_asset(PYCON_URL + url)


def script(soup):
    for script in soup.find_all("script"):
        # get all url like /year/... target, and try to save them all.
        all_url = re.findall("/" + PYCON_YEAR + r"[^\s]*", str(script))
        for url in all_url:
            url = url[0 : max(url.rfind("'"), url.rfind('"'))]
            if not Path("." + url).exists():
                get_asset(PYCON_URL + url)



def css(soup):
    for css in soup.find_all("link"):
        # if the link tag has the 'href' attribute and
        # if the target is css file and not using outer css site
        if (
            css.attrs.get("href")
            and css["href"].find("https://") == -1
            and css["href"].find("css") != -1
            and not Path("." + css["href"]).exists()
        ):
            get_asset(PYCON_URL + css["href"])
            getcssimg(css["href"])
            with open("." + css["href"], "r") as f:
                css_file = f.read()
            css_file = css_file.replace("url('", f"url('{BASE_URL}")
            css_file = css_file.replace('url("', f'url("{BASE_URL}')
            css_file = css_file.replace("url(/", f"url({BASE_URL}/")
            with open("." + css["href"], "w") as f:
                f.write(css_file)


def img(soup):
    for img in soup.find_all("img"):
        # if img has attr src
        if img.attrs.get("src"):
            get_asset(img["src"])
    # get imgs in json, especially for pycon /2017/zh-hant/events/keynotes/
    for script in soup.find_all("script", type="application/json"):
        json_object = json.loads(script.contents[0])
        if "keynote" in json_object:
            for person in json_object["keynote"]:
                get_asset(person["photo"])


def get_page(crawler: BaseCrawler, url: str):
    path = urlparse(url).path
    # Don't crawl same page again in case of infinite loop
    if Path("." + path + "index.html").exists():
        return

    soup = get_soup(url)
    script(soup)  # get scripts in this page
    css(soup)  # get css in this page
    img(soup)  # get imgs in this page
    # save the html
    # 1) for supporting 2 languages, each pycon year will deal separately.
    # 2) by using unquote to avoid the Garbled path
    mkdir(path)
    for input in soup.find_all("input", {"name": "csrfmiddlewaretoken"}):
        input.decompose()
    if PYCON_YEAR == "2017":
        if path[6:8] == "zh":
            elements = soup.find_all("a", {"data-lang": "en-us"})
            for elm in elements:
                elm.replace_with("en-us_target")
        if path[6:8] == "en":
            elements = soup.find_all("a", {"data-lang": "zh-hant"})
            for elm in elements:
                elm.replace_with("zh-hant_target")

    html = crawler.convert_html(path, soup)
    with open("." + path + "index.html", "w") as f:
        f.write(unquote(html))

    # get talk and tutorial page
    for link in soup.find_all("a"):
        if (
            not link.attrs.get("href")
            or link["href"].find("https://") != -1
            or link["href"].find("#") != -1
        ):
            continue
        if (
            link.get("href").find("talk") != -1
            or link.get("href").find("tutorial") != -1
        ):
            get_page(crawler, unquote(link["href"]))


def main():
    crawler: BaseCrawler = CRAWLERS[PYCON_YEAR](PYCON_URL, PYCON_YEAR)
    crawler_urls = crawler.get_crawl_urls()

    # Page crawler section
    for crawler_url in crawler_urls:
        url = urlparse(crawler_url)
        # Checking if the url is a pycon website
        if url.netloc != crawler.host and url.netloc != "":
            continue
        # Checking if the path is right or not
        if url.netloc == "" and url.path.find(f"/{crawler.year}") != 0:
            continue
        path_parts = Path(url.path).parts
        if len(path_parts) >= 2 and path_parts[1] == crawler.year:
            get_page(crawler, crawler_url)
            get_page(crawler, crawler_url.replace("zh-hant", "en-us"))

    # Get favicon on front page
    soup = get_soup(f"{crawler.url}/{crawler.year}/zh-hant/")
    for link in soup.findAll("link", {"rel": "icon"}):
        if "href" in link.attrs:
            get_asset(link["href"])


@click.command()
@click.option(
    "-y",
    "param",
    help="Pycon Year (2016 - 2020)",
    type=click.DateTime(formats=["%Y"]),
    required=True,
)
@click.option(
    "--base", "base_url", help="The base url for all site", type=str, required=False
)
def check_year(param, base_url):
    """Get Pycon Website According To the Year"""
    global PYCON_YEAR
    global BASE_URL  # TODO: [Refactor] to encapuslate all the global variable
    if base_url is None:
        BASE_URL = ''
    else:
        BASE_URL = base_url
    PYCON_YEAR = str(param.year)
    if PYCON_YEAR >= "2016" and PYCON_YEAR <= "2020":
        main()
    else:
        logger.error("Pycon Year Should be between 2016 and 2020 !")


if __name__ == "__main__":
    check_year()
