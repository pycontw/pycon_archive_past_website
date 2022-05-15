from pathlib import Path
from urllib.parse import urlparse

import click
from crawlers import CRAWLERS, BaseCrawler
from loguru import logger


def main(year: str, base_url: str):
    try:
        crawler: BaseCrawler = CRAWLERS[year]("https://tw.pycon.org", base_url)
    except KeyError:
        raise Exception(f"Crawler with year {year} does not exist!")
    print(1)
    crawler.crawl_favicon()
    # Page crawler section
    # for crawler_url in crawler.get_crawl_urls():
    #     url = urlparse(crawler_url)
    #     # Checking if the url is a pycon website
    #     if url.netloc != crawler.host and url.netloc != "":
    #         continue
    #     # Checking if the path is right or not
    #     if url.netloc == "" and url.path.find(f"/{crawler.year}") != 0:
    #         continue
    #     path_parts = Path(url.path).parts
    #     if len(path_parts) >= 2 and path_parts[1] == crawler.year:
    #         crawler.crawl_page(crawler_url)
    #         crawler.crawl_page(crawler_url.replace("zh-hant", "en-us"))


@click.command()
@click.option(
    "-y",
    "param",
    help="Pycon Year (2016 - 2020)",
    type=str,
    required=True,
)
@click.option(
    "--base",
    "base_url",
    help="The base url for all site",
    type=str,
    required=False,
    default="",
)
def check_year(param, base_url):
    """Get Pycon Website According To the Year"""
    try:
        main(param, base_url)
    except Exception as error:
        logger.error(error)


if __name__ == "__main__":
    check_year()
