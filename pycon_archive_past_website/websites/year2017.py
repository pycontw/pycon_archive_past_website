import json

from bs4 import BeautifulSoup

from .classes import BaseCrawler
from .utilities import get_asset, get_language


class Year2017(BaseCrawler):

    year: str = "2017"

    def preprocess_soup(self, path: str, soup: BeautifulSoup) -> BeautifulSoup:
        if get_language(path) == "zh":
            elements = soup.find_all("a", {"data-lang": "en-us"})
            for elm in elements:
                elm.replace_with("en-us_target")
        if get_language(path) == "en":
            elements = soup.find_all("a", {"data-lang": "zh-hant"})
            for elm in elements:
                elm.replace_with("zh-hant_target")
        return soup

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

    def get_image(self, soup: BeautifulSoup):
        super().get_image(soup)
        # get imgs from json, especially for pycon /2017/zh-hant/events/keynotes/
        for script_element in soup.find_all("script", type="application/json"):
            json_object = json.loads(script_element.contents[0])
            if "keynote" in json_object:
                for person in json_object["keynote"]:
                    get_asset(person["photo"])
