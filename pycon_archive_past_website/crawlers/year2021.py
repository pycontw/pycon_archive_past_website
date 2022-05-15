from typing import MutableSet

from bs4 import BeautifulSoup
from common.scrape import get_soup

from .base import BaseCrawler
from .utilities import get_language

from crawlers.utilities import get_asset


class Year2021(BaseCrawler):

    year: str = "2021"

    def get_crawl_urls(self) -> MutableSet[str]:
        urls = super().get_crawl_urls()
        print(f"now base urls is {urls}")
        # soup = get_soup(f"{self.url}/{self.year}/zh-hant/events/warmup-session/")
        # for url in soup.select("a"):
        #     url = url["href"]
        #     urls.add(url)
        #     print(f"2021 warmup-session find a url {url}")
        urls.add(f"{self.url}/{self.year}/zh-hant/sponsor/prospectus/")
        # change the url if startwith /2021
        # for url in urls:
        #     print(url.find(f"/{self.year}"), url)

        urls = [f"{self.url}{url}" if url.find(f"/{self.year}") == 0 else url for url in urls]
        urls = [url if url[-1] == '/' else url + '/' for url in urls]
        
        print(f"after adding self.url: {urls}")
        return set(urls)

    def convert_html(self, path: str, soup: BeautifulSoup) -> str:
        html = super().convert_html(path, soup)
        full_path = self.base_path + path
        if get_language(path) == "zh":
            print(f"2021 convert html zh")
            html = html.replace(
                "EN",
                "<a href='"
                + full_path.replace("zh-hant", "en-us")
                + '\' style="text-decoration: none;">EN</a>',
                1,
            )
        if get_language(path) == "en":
            print(f"2021 convert html en")
            html = html.replace(
                "ZH",
                "<a href='"
                + full_path.replace("en-us", "zh-hant")
                + '\' style="text-decoration: none;">ZH</a>',
                1,
            )
        return html

    def crawl_favicon(self):
        """
        Download favicon on front page
        """
        print(f"2021 favicon:  {self.url},.. {self.year}")
        soup = get_soup(f"{self.url}/{self.year}/zh-hant/")
        for link in soup.findAll("link", {"rel": "icon"}):
            if "href" in link.attrs:
                print(f"find a href in favicon {link}")
                link = self.url + link["href"]
                print(link)
                get_asset(link)
