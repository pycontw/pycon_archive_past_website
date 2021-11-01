"""
    Crawler related functions.
    Usually combined function of common modules
"""
from urllib.parse import urlparse

import requests

from common.dataio import mkdir, writefile


def get_asset(url: str):
    """
        Get asset in the given url.

        Args:
            url (str): Website url
    """
    path: str = urlparse(url).path
    request = requests.get(url, allow_redirects=True)
    mkdir(path)
    writefile(path, request.content)


def get_language(path: str):
    """
        Get website language in url path
        Args:
            path (str): path
    """
    # The path are in the following format:
    # <optional base_url>/<year>/<lang>/....
    # ex: /2021/zh-hant/about/history, /2015apac/en/about/index.html, /2019/en-us/
    # Use for loop to find language
    for part in path.split("/"):
        if 'en' in part:
            return 'en'
        if 'zh' in part:
            return 'zh'
    return 'en'
