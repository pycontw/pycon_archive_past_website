from typing import MutableSet

from bs4 import BeautifulSoup
from common.scrape import get_soup
from loguru import logger

from .base import BaseCrawler
from .utilities import get_language

from crawlers.utilities import get_asset


class Year2021(BaseCrawler):

    year: str = "2021"

    def get_candidate_urls(self) -> MutableSet[str]:
        urls = super().get_candidate_urls()

        urls.add(f"{self.url}/{self.year}/zh-hant/sponsor/prospectus/")

        urls = {f"{self.url}{url}" if url.find(f"/{self.year}") == 0 else url for url in urls}
        urls = {url if url[-1] == '/' else url + '/' for url in urls}

        logger.debug(f"candidate URLs: {urls=}")
        return set(urls)

    def convert_html(self, path: str, soup: BeautifulSoup) -> str:
        html = super().convert_html(path, soup)
        full_path = self.base_path + path
        if get_language(path) == "zh":
            logger.info("converting to zh-hant version of HTML")
            html = html.replace(
                "EN",
                "<a href='"
                + full_path.replace("zh-hant", "en-us")
                + '\' style="text-decoration: none;">EN</a>',
                1,
            )
        if get_language(path) == "en":
            logger.info("converting to EN version of HTML")
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
        logger.debug(f"favicon:  {self.url=} {self.year=}")
        soup = get_soup(f"{self.url}/{self.year}/zh-hant/")
        for link in soup.findAll("link", {"rel": "icon"}):
            if "href" in link.attrs:
                link = self.url + link["href"]
                logger.info(f"find a href in favicon {link=}")
                get_asset(link)
