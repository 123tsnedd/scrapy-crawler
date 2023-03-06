import scrapy


class PriceSpider(scrapy.Spider):
    name = "price"
    allowed_domains = ["www.google.com"]
    start_urls = ["http://www.google.com/"]

    def parse(self, response):
        pass


"""scrapy shell
fetch('url') gets info on page and saves to response
can just type 'response' to see while in shell
response.css('a::attr(href)').getall()to get urls
"""

import scrapy
import re


def seperateUrl(url):
    split_url = url.split(
        "&"
    )  # splits the url to extract just the forwarding html portion. 0

    return split_url[0][7:]  # Hard coded to skip to the http


class price_spider(scrapy.Spider):
    name = "shopper"

    urls = [
        "https://www.google.com/search?q=menloafers"  # + input("search: ")
    ]  # use google as search eng

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(
                url=url, callback=self.parse
            )  # call results back to parse

    def parse(self, response):  # all info scrapy retrieves is held in response
        for url in response.css("a::attr(href)").getall():
            if "http" in url and "google" not in url:
                yield {
                    "url": seperateUrl(url),
                    "site_name": re.findall(r"\w+.com\b", url),
                }


class google_shop(scrapy.Spider):
    name = "pricer"

    url = []


#
# find the name of site
# re.findall(r"\w+.com\b", url)
