"""Data related functions"""
from pathlib import Path
from urllib.parse import unquote, urlparse

from loguru import logger


def mkdir(path: str):
    """
    Create folder from execute entry folder

    Args:
        path (str): File path, ex: 2016/index.html
    """
    path = urlparse(path).path
    try:
        # correct the path to directory path and be a local path
        dir = Path("./" + unquote(path)).parent.resolve()
        dir.mkdir(parents=True, exist_ok=True)
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
