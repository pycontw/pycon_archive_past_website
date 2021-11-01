import os
from urllib.parse import unquote, urlparse

import requests
from loguru import logger

PYCON_URL = f"https://tw.pycon.org"


def mkdir(path: str):
    path = urlparse(path).path
    try:
        # 1) correct the path to directory path and be a local path
        # 2) by using unquote to avoid the Garbled path
        dir = "." + path[0 : path.rfind("/") + 1]
        dir = unquote(dir)
        if not os.path.exists(os.path.dirname(dir)):
            os.makedirs(dir)
    except OSError as err:
        logger.error(err)


def writefile(path: str):
    # request to the Pycon path, and fetch it to local file by using binary writing
    path = urlparse(path).path
    request = requests.get(PYCON_URL + path)
    file = "." + unquote(path)
    try:
        with open(file, "wb") as f:
            f.write(request.content)
    except OSError as err:
        logger.error(err)
