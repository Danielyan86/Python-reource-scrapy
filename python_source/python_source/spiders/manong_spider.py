import scrapy


class manong(scrapy.Spider):
    name = "manong"
    allowed_domains = ["weekly.manong.io/"]
    start_urls = ["http://weekly.manong.io/issues/"]
    for number in range(1, 106):
        start_urls.append("http://weekly.manong.io/issues/{0}".format(number))

    def parse(self, response):
        print "this is response", response
        # filename = "./files/" + response.url.split('/')[-1] + ".html"
        filename = "./files/ " + "manong_python_reource.html"

        p = response.xpath('//h4').extract()
        with open(filename, "a+") as f:
            for item in p:
                if u"python" in item or u"Python" in item:
                    f.write(item.encode("utf-8"))
                    f.write("\n")
