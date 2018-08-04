# -*- coding: utf-8 -*-
import scrapy
from flights.items import CitiesItem


class CitiesSpider(scrapy.Spider):
    name = 'cities'
    start_url = 'http://www.6qt.net/index.asp?Field=Code&keyword=CN&MaxPerPage=50&page={page}'

    def start_requests(self):
        for i in range(1, 5):
            url = self.start_url.format(page=i)
            yield scrapy.Request(url)

    def parse(self, response):
        rows = response.xpath('/html/body/table[3]//tr[.//a]')
        for row in rows:
            item = CitiesItem()
            item['city'] = row.xpath('./td[1]/a/text()').extract_first()
            item['code'] = row.xpath('./td[2]/a/text()').extract_first()
            item['airport'] = row.xpath('./td[6]/text()').extract_first()
            yield item
