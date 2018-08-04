# -*- coding: utf-8 -*-
import scrapy
from flights.items import AirlinesItem


class AirlinesSpider(scrapy.Spider):
    name = 'airlines'
    start_urls = ['https://baike.baidu.com/item/%E8%88%AA%E7%A9%BA%E5%85%AC%E5%8F%B8%E4%BB%A3%E7%A0%81%E8%A1%A8/4130979']

    def parse(self, response):
        rows = response.xpath('/html/body/div[3]/div[2]/div/div[2]/table/tr[string-length(./td[3]//text()) = 2]')
        for row in rows:
            item = AirlinesItem()
            item['name'] = row.xpath('./td[1]//text()').extract_first()
            item['code'] = row.xpath('./td[3]//text()').extract_first()
            yield item
