"""Data related functions"""
import os
from urllib.parse import unquote, urlparse

from loguru import logger


def mkdir(path: str):
    """
    Create folder from execute entry folder

    Args:
        path (str): relative path
    """
    path = urlparse(path).path
    try:
        # correct the path to directory path and be a local path
        dir = "." + path[0 : path.rfind("/") + 1]
        # unquote to avoid the Garbled path
        dir = unquote(dir)
        if not os.path.exists(os.path.dirname(dir)):
            os.makedirs(dir)
    except OSError as err:
        logger.error(err)


def writefile(path: str, content: bytes):
    """
    Write file to related path from execute entry folder

    Args:
        path (str): relative path
        content (bytes): Object to be written
    """
    path = urlparse(path).path
    try:
        file = "." + unquote(path)
        with open(file, "wb") as f:
            f.write(content)
    except OSError as err:
        logger.error(err)
