from typing import MutableSet
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


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
        request = requests.get(f"{self.url}/{self.year}/zh-hant/")
        soup = BeautifulSoup(request.text, "html.parser")
        return set([crawler_url["href"] for crawler_url in soup.select("a")])
