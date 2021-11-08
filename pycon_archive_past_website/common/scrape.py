"""Data crawling related functions"""
import requests
from bs4 import BeautifulSoup
from loguru import logger


def get_soup(url: str) -> BeautifulSoup:
    """
        Get BeautifulSoup HTML document by url.

    Args:
        url (str): Request URL

    Returns:
        BeautifulSoup: HTML document
    """
    logger.info(f"Fetching {url}")
    request = requests.get(url)
    return BeautifulSoup(request.text, "html.parser")
