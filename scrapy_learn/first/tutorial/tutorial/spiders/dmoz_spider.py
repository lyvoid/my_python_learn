import scrapy
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    # allowed_domains = ["2345.com/"]
    start_urls = [
        "http://www.2345.com"
    ]

    def parse(self, response):
        for sel in response.xpath("//a"):
            item = DmozItem()
            item['title'] = sel.xpath('text()').extract()
            item['link'] = sel.xpath('@href').extract()
            item['class_'] = sel.xpath('@class').extract()
            yield item
        # for url in response.xpath('//a/@href').extract():
        #     yield scrapy.Request(url, callback=self.parse)
