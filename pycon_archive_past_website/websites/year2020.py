from typing import MutableSet


from common.scrap import get_soup
from .classes import BaseCrawler


class Year2020(BaseCrawler):

    def get_crawl_urls(self) -> MutableSet[str]:
        urls = super().get_crawl_urls()
        soup = get_soup(f"{self.url}/{self.year}/zh-hant/events/warmup-session/")
        for url in soup.select("a"):
            url = url["href"]
            urls.add(url)
        urls.add(f"{self.url}/{self.year}/zh-hant/sponsor/prospectus/")
        return set(urls)
