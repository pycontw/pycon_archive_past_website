from bs4 import BeautifulSoup

from .classes import BaseCrawler
from .utilities import get_language


class Year2017(BaseCrawler):

    def convert_html(self, path: str, soup: BeautifulSoup) -> str:
        html = super().convert_html(path, soup)
        full_path = self.base_path + path
        if get_language(path) == "zh":
            html = html.replace(
                "en-us_target",
                '<div data-lang="en-us" style="margin-left: 40px; line-height: 60px;"> <a href=\''
                + full_path.replace("zh-hant", "en-us")
                + '\' style="font-size: 16px;">English (US)</a></div>',
                1,
            )
            html = html.replace(
                "en-us_target",
                '<div data-lang="en-us" style="margin-left: 20px;"> <a href=\''
                + full_path.replace("zh-hant", "en-us")
                + "'>English (US)</a></div>",
                1,
            )
        if get_language(path) == "en":
            html = html.replace(
                "zh-hant_target",
                '<div data-lang="zh-hant" style="margin-left: 40px; line-height: 60px;"> <a href=\''
                + full_path.replace("en-us", "zh-hant")
                + '\' style="font-size: 16px;">繁體中文</a></div>',
                1,
            )
            html = html.replace(
                "zh-hant_target",
                '<div data-lang="zh-hant" style="margin-left: 20px;"> <a href=\''
                + full_path.replace("en-us", "zh-hant")
                + "'>繁體中文</a></div>",
                1,
            )
        return html
