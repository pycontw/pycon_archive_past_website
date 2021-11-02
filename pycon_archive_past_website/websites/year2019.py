from bs4 import BeautifulSoup

from .classes import BaseCrawler
from .utilities import get_language


class Year2019(BaseCrawler):

    year: str = "2019"

    def convert_html(self, path: str, soup: BeautifulSoup) -> str:
        html = super().convert_html(path, soup)
        full_path = self.base_path + path
        if get_language(path) == "zh":
            html = html.replace(
                "EN",
                "<a href='"
                + full_path.replace("zh-hant", "en-us")
                + '\' class="myclass">EN</a>',
                1,
            )
        if get_language(path) == "en":
            html = html.replace(
                "ZH",
                "<a href='"
                + full_path.replace("en-us", "zh-hant")
                + '\' class="myclass">ZH</a>',
                1,
            )
        html += "<style>.myclass{text-decoration: none;color: #616e86;}.myclass:hover{text-decoration: none;color: #4a5363;}</style>"
        return html
