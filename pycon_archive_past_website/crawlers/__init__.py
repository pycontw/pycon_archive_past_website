from typing import Dict, Type

from .base import BaseCrawler
from .year2014 import Year2014
from .year2016 import Year2016
from .year2017 import Year2017
from .year2018 import Year2018
from .year2019 import Year2019
from .year2020 import Year2020

CRAWLERS: Dict[str, Type[BaseCrawler]] = {
    "2014": Year2014,
    "2016": Year2016,
    "2017": Year2017,
    "2018": Year2018,
    "2019": Year2019,
    "2020": Year2020,
}
