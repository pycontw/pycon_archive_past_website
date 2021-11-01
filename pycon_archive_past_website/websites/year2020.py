from typing import MutableSet

from .classes import BaseCrawler

import requests
from bs4 import BeautifulSoup


class Year2020(BaseCrawler):

    def get_crawl_urls(self) -> MutableSet[str]:
        urls = super().get_crawl_urls()
        request = requests.get(self.url + "/" + self.year + "/zh-hant/events/warmup-session/")
        soup = BeautifulSoup(request.text, "html.parser")
        for url in soup.select("a"):
            url = url["href"]
            urls.add(url)
        urls.add(f"{self.url}/{self.year}/zh-hant/sponsor/prospectus/")
        return set(urls)
