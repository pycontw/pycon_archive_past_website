"""Crawler related classes"""
from typing import MutableSet
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from common.scrap import get_soup


class BaseCrawler():

    host: str
    url: str
    year: str
    base_path: str

    def __init__(self, pycon_url: str, year: str, base_path: str = '') -> None:
        """
            Args:
                pycon_url (str): PyCon URL, ex: https://tw.pycon.org
                year (str): PyCon year, ex: 2016
                base_url (str, optional): Path prefix for Github pages. Defaults to ''.
        """
        self.host = urlparse(pycon_url).netloc
        self.url = pycon_url
        self.year = year
        self.base_path = base_path

    def get_crawl_urls(self) -> MutableSet[str]:
        """
            Get URLs should be crawled

            Returns:
                MutableSet[str]: Set of urls
        """
        soup = get_soup(f"{self.url}/{self.year}/zh-hant/")
        return set([crawler_url["href"] for crawler_url in soup.select("a")])

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
