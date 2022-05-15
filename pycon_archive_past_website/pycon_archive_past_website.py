from pathlib import Path
from urllib.parse import urlparse

import click
from crawlers import CRAWLERS, BaseCrawler
from loguru import logger


def main(year: str, base_url: str):
    try:
        crawler: BaseCrawler = CRAWLERS[year]("https://tw.pycon.org", base_url)
        print(crawler)
    except KeyError:
        raise Exception(f"Crawler with year {year} does not exist!")
    print("2021 crawl favicon")
    crawler.crawl_favicon()
    print("2021 crawl favicon finished")
    # Page crawler section
    for crawler_url in crawler.get_crawl_urls():
        url = urlparse(crawler_url)
        # print(f"2021 {url}")
        # Checking if the url is a pycon website
        if url.netloc != crawler.host and url.netloc != "":
            # print(f"case 1 continue {url}")
            continue
        # Checking if the path is right or not
        if url.netloc == "" and url.path.find(f"/{crawler.year}") != 0:
            # print(f"case 2 contunue {url}")
            continue
        path_parts = Path(url.path).parts
        if len(path_parts) >= 2 and path_parts[1] == crawler.year:
            print(f"need to crawl, {crawler_url}, parts={path_parts}")
            crawler.crawl_page(crawler_url)
            crawler.crawl_page(crawler_url.replace("zh-hant", "en-us"))



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
