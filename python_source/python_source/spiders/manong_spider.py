import scrapy
from ..items import PythonSourceItem


class manong(scrapy.Spider):
    name = "manong"
    allowed_domains = ["weekly.manong.io/"]
    start_urls = ["http://weekly.manong.io/issues/"]
    issue_number = 143 # Issue number should be less than current issue number
    for number in range(1, issue_number):
        start_urls.append("http://weekly.manong.io/issues/{0}".format(number))

    filename = "./files/" + "manong_python_reource.html"
    def parse(self, response):
        print "this is response", response
        # filename = "./files/" + response.url.split('/')[-1] + ".html"


        p = response.xpath('//h4').extract()
        item_dic = PythonSourceItem()
        # items = []
        # for i in p:
        #     item_dic['desc'] = unicode(i)
        #     items.append(item_dic)
        # return items
        with open(self.filename, "a+") as f:
            for item in p:
                if u"python" in item or u"Python" in item:
                    f.write(item.encode("utf-8"))
                    f.write("\n")
