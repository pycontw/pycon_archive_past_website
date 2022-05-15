from typing import MutableSet

from bs4 import BeautifulSoup
from common.scrape import get_soup

from .base import BaseCrawler
from .utilities import get_language


class Year2020(BaseCrawler):

    year: str = "2020"

    def get_crawl_urls(self) -> MutableSet[str]:
        urls = super().get_crawl_urls()
        soup = get_soup(f"{self.url}/{self.year}/zh-hant/events/warmup-session/")
        for url in soup.select("a"):
            url = url["href"]
            urls.add(url)
        urls.add(f"{self.url}/{self.year}/zh-hant/sponsor/prospectus/")
        return set(urls)

    def convert_html(self, path: str, soup: BeautifulSoup) -> str:
        html = super().convert_html(path, soup)
        full_path = self.base_path + path
        if get_language(path) == "zh":
            print(f"2020 convert html zh")
            html = html.replace(
                "EN",
                "<a href='"
                + full_path.replace("zh-hant", "en-us")
                + '\' style="text-decoration: none;">EN</a>',
                1,
            )
        if get_language(path) == "en":
            print(f"2020 convert html en")
            html = html.replace(
                "ZH",
                "<a href='"
                + full_path.replace("en-us", "zh-hant")
                + '\' style="text-decoration: none;">ZH</a>',
                1,
            )
        return html
