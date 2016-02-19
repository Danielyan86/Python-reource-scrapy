import scrapy


class manong_spider(scrapy.Spider):
    name = "manong"
    allowed_domains = ["tubemogul.com"]
    start_urls = ["http://www.tubemogul.com"]

    def parse(self, response):
        print "this is response", response
