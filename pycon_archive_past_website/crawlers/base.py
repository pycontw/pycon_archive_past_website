"""Crawler related classes"""
import re
from pathlib import Path
from typing import MutableSet
from urllib.parse import unquote, urlparse

from bs4 import BeautifulSoup
from common.scrape import get_soup
from crawlers.utilities import get_asset, mkdir


class BaseCrawler:

    host: str  # Network location, ex: tw.pycon.org
    url: str  # Host full path, ex: https://tw.pycon.org
    year: str  # pycon year prefix, should be assigned in subclasses
    base_path: str  # path prefix used in Github pages

    def __init__(self, pycon_url: str, base_path: str = "") -> None:
        """
        Args:
            pycon_url (str): PyCon URL, ex: https://tw.pycon.org
            base_url (str, optional): Path prefix for Github pages. Defaults to ''.
        """
        self.host = urlparse(pycon_url).netloc
        self.url = pycon_url
        self.base_path = base_path

    def get_crawl_urls(self) -> MutableSet[str]:
        """
        Get URLs should be crawled

        Returns:
            MutableSet[str]: Set of urls
        """
        soup = get_soup(f"{self.url}/{self.year}/zh-hant/")
        return set([crawler_url["href"] for crawler_url in soup.select("a")])

    def preprocess_soup(self, path: str, soup: BeautifulSoup) -> BeautifulSoup:
        """
            Preprocess HTML document for later HTML conversion(convert_html)

        Args:
            path (str): URL path, ex: /2020/en-us
            soup (BeautifulSoup): HTML document

        Returns:
            BeautifulSoup: Processed HTML document
        """
        return soup

    def convert_html(self, path: str, soup: BeautifulSoup) -> str:
        """
            Convert each year's HTML page translation

        Args:
            path (str): URL path, ex: /2020/en-us
            soup (BeautifulSoup): HTML document

        Returns:
            str: Converted HTML document
        """
        html = str(soup)
        html = html.replace('method="post"', "")
        html = html.replace(f'action="/{self.year}/set-language/"', "")
        if path.startswith(f"/{self.year}"):
            # Replace url prefix since the gh-pages use base url following `{host}/{repo}/` instead of {host}/
            html = html.replace(f"/{self.year}/", f"{self.base_path}/{self.year}/")
        return html

    def crawl_script(self, soup: BeautifulSoup):
        """
            Download Javascript files from HTML document

        Args:
            soup (BeautifulSoup): HTML document
        """
        for script in soup.find_all("script"):
            # get all url like /year/... target, and try to save them all.
            for path in re.findall("/" + self.year + r"[^\s]*", str(script)):
                path = path[0 : max(path.rfind("'"), path.rfind('"'))]
                if not Path("." + path).exists():
                    get_asset(self.url + path)

    def crawl_image(self, soup: BeautifulSoup):
        """
            Download image files from HTML document

        Args:
            soup (BeautifulSoup): HTML document
        """
        for image_element in soup.find_all("img"):
            # if img has attr src
            if image_element.attrs.get("src"):
                get_asset(image_element["src"])

    def crawl_stylesheet(self, soup: BeautifulSoup):
        """
            Download CSS files from HTML document

        Args:
            soup (BeautifulSoup): HTML document
        """
        for css in soup.find_all("link"):
            # if the link tag has the 'href' attribute and
            # if the target is css file and not using outer css site
            if (
                css.attrs.get("href")
                and css["href"].find("https://") == -1
                and css["href"].find("css") != -1
                and not Path("." + css["href"]).exists()
            ):
                # Download CSS, read and then rewrite it
                get_asset(self.url + css["href"])
                with open("." + css["href"], "r") as f:
                    css_file = f.read()
                css_file = css_file.replace("url('", f"url('{self.base_path}")
                css_file = css_file.replace('url("', f'url("{self.base_path}')
                css_file = css_file.replace("url(/", f"url({self.base_path}/")
                with open("." + css["href"], "w") as f:
                    f.write(css_file)

    def crawl_favicon(self):
        print(3)
        """
        Download favicon on front page
        """
        print(f"{self.url}/{self.year}/zh-hant/")
        soup = get_soup(f"{self.url}/{self.year}/zh/")
        for link in soup.findAll("link", {"rel": "icon"}):
            if "href" in link.attrs:
                print(link["href"])
                get_asset(link["href"])

    def crawl_page(self, url: str):
        """
            Download HTML document

        Args:
            url (str): URL, ex: https://tw.pycon.org/2020/en-us/
        """
        # concate to <path>/index.html
        path = f"{urlparse(url).path}index.html"
        # Do not crawl page if already exists, prevent recursive traversal
        if Path(f"./{path}").exists():
            return
        print(1)
        mkdir(path)
        soup = get_soup(url)
        # self.crawl_script(soup)
        # self.crawl_stylesheet(soup)
        # self.crawl_image(soup)

        for input in soup.find_all("input", {"name": "csrfmiddlewaretoken"}):
            input.decompose()
        soup = self.preprocess_soup(path, soup)
        html = self.convert_html(path, soup)

        # use unquote to avoid the Garbled path
        with open(f"./{path}", "w",encoding='utf_8') as f:
            f.write(unquote(html))

        # get talk and tutorial page using DFS
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
                self.crawl_page(unquote(link["href"]))
