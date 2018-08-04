# -*- coding: utf-8 -*-
import scrapy
import json
from flights.items import FlightsItem
import datetime


class CtripFlightsSpider(scrapy.Spider):
    name = 'ctrip_flights'
    start_url = 'http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1={dcity}&ACity1={acity}&SearchType=S&DDate1={ddate1}'

    def start_requests(self):
        time = '2018-8-19'
        cities = json.load(open('outputs/cities.json', 'r'))
        for d in cities:
            dcity = d['code']
            for a in cities:
                acity = a['code']
                if dcity == acity:
                    continue
                url = self.start_url.format(dcity=dcity, acity=acity, ddate1=time)
                yield scrapy.Request(
                    url,
                    cookies={
                        '_RSG': 'FFaqxQlNGF9cQFKaUGSen8',
                        '_RDG': '28fc90eb234f1729ea1c1491b0bdb73881',
                        '_RGUID': '93d05ef6-bbd2-43cf-8c68-7107a450f6a6'
                    }
                )

    def parse(self, response):
        fis = json.loads(response.body.decode('gb2312'))['fis']
        for flight in fis:
            item = FlightsItem()
            item['airline'] = flight['alc']
            item['flight'] = flight['fn']
            item['departure'] = flight['dpc']
            item['arrival'] = flight['apc']
            item['departure_time'] = flight['dt']
            item['arrival_time'] = flight['at']
            item['price'] = flight['lp']
            item['crawl_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            yield item
