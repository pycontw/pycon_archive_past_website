from bs4 import BeautifulSoup

from .base import BaseCrawler


class Year2016(BaseCrawler):

    year: str = "2016"

    def convert_html(self, path: str, soup: BeautifulSoup) -> str:
        html = super().convert_html(path, soup)
        full_path = self.base_path + path
        html = html.replace(
            '<a data-lang="zh-hant" href="#">',
            '<a data-lang="zh-hant" href="'
            + full_path.replace("en-us", "zh-hant")
            + '">',
        )
        html = html.replace(
            '<a data-lang="en-us" href="#">',
            '<a data-lang="en-us" href="'
            + full_path.replace("zh-hant", "en-us")
            + '">',
        )
        return html
