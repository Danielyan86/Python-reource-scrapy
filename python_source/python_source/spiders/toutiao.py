import scrapy


class toutiao(scrapy.Spider):
    name = "toutiao"
    allowed_domains = ["toutiao.io/"]
    start_urls = ["http://toutiao.io/search?q=python&utf8=%E2%9C%93"]
    for number in range(2, 38):
        start_urls.append("http://toutiao.io/search?page={0}&q=python&utf8=%E2%9C%93".format(number))

    def parse(self, response):
        print "this is response", response
        # filename = "./files/" + response.url.split('/')[-1] + ".html"
        filename = "./files/ " + "toutiao.html"

        p = response.xpath('//div[@class="content"]').extract()
        with open(filename, "a+") as f:
            for item in p:
                if u"python" in item or u"Python" in item:
                    f.write(item.encode("utf-8"))
                    f.write("\n")
