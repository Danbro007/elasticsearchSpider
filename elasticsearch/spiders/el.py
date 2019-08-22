# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class ElSpider(scrapy.Spider):
    name = 'el'
    allowed_domains = ['elasticsearch.cn']
    start_urls = ['https://elasticsearch.cn/']
    start_url = "https://elasticsearch.cn/sort_type-new__day-0__is_recommend-0__page-{page}"

    def start_requests(self):
        for i in range(1):
            yield Request(url=self.start_url.format(page=i + 1), callback=self.indexParse)

    def indexParse(self, response):
        questionHrefList = response.xpath("//div[@class='aw-common-list']//div[@class='aw-question-content']//h4")
        for questionHref in questionHrefList:
            href = questionHref.xpath(".//@href").extract_first()
            yield Request(url=href, callback=self.questionParse)

    def questionParse(self, response):
        title = response.xpath("/html/body/div[2]/div/div/div/div[1]/div[1]/div[1]/h1/text()").extract_first().strip()
        author = response.xpath(
            "/html/body/div[2]/div/div/div/div[1]/div[1]/div[1]/em/a[2]/text()").extract_first().strip()
        description = response.xpath(
            "/html/body/div[2]/div/div/div/div[1]/div[1]/div[2]/div/text()").extract_first().strip()
        print("标题:", title)
        print("作者:", author)
        print("内容:", description)
        print("\n")
