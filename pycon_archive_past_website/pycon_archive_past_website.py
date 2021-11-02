from pathlib import Path
from urllib.parse import unquote, urlparse

import click
from common.dataio import mkdir
from common.scrap import get_soup
from loguru import logger
from websites import CRAWLERS, BaseCrawler
from websites.utilities import get_asset


def get_page(crawler: BaseCrawler, url: str):
    path = urlparse(url).path
    mkdir(path)
    # Don't crawl same page again in case of infinite loop
    if Path("." + path + "index.html").exists():
        return

    soup = get_soup(url)
    crawler.get_script(soup)
    crawler.get_stylesheet(soup)
    crawler.get_image(soup)

    for input in soup.find_all("input", {"name": "csrfmiddlewaretoken"}):
        input.decompose()
    soup = crawler.preprocess_soup(path, soup)
    html = crawler.convert_html(path, soup)

    # use unquote to avoid the Garbled path
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


def main(year: str, base_url: str):
    crawler: BaseCrawler = CRAWLERS[year]("https://tw.pycon.org", base_url)
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
    "--base",
    "base_url",
    help="The base url for all site",
    type=str,
    required=False,
    default="",
)
def check_year(param, base_url):
    """Get Pycon Website According To the Year"""
    year: str = str(param.year)
    if year >= "2016" and year <= "2020":
        main(year, base_url)
    else:
        logger.error("Pycon Year Should be between 2016 and 2020 !")


if __name__ == "__main__":
    check_year()
