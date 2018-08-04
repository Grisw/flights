# -*- coding: utf-8 -*-
import scrapy
import json


class CtripFlightsSpider(scrapy.Spider):
    name = 'ctrip_flights'
    start_url = 'http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1={dcity}&ACity1={acity}&SearchType=S&DDate1={ddate1}'

    def start_requests(self):
        url = self.start_url.format(dcity='SHA', acity='CAN', ddate1='2018-8-19')
        yield scrapy.Request(
            url,
            cookies={
                # '_abtest_userid': '6f13cde3-c1de-4816-b1d6-e7f53c78b1c1',
                '_RSG': 'FFaqxQlNGF9cQFKaUGSen8',
                '_RDG': '28fc90eb234f1729ea1c1491b0bdb73881',
                '_RGUID': '93d05ef6-bbd2-43cf-8c68-7107a450f6a6',
                # '_ga': 'GA1.2.1124673856.1530676098',
                # 'traceExt': 'campaign=CHNbaidu81&adid=index',
                # 'Union': 'SID=155952&AllianceID=4897&OUID=baidu81|index|||',
                # 'adscityen': 'Ningde',
                # '_RF1': '120.43.43.119',
                # '_gid': 'GA1.2.1157551365.1533350731',
                # 'MKT_Pagesource': 'PC',
                # 'Session': 'SmartLinkCode=jb51&SmartLinkKeyWord=&SmartLinkQuary=_UTF.&SmartLinkHost=www.jb51.net&SmartLinkLanguage=zh',
                # 'FD_SearchHistorty': '{"type":"S","data":"S%24%u4E0A%u6D77%28SHA%29%24SHA%242018-08-14%24%u6B66%u6C49%28WUH%29%24WUH%24%24%24"}',
                # '_bfa': '1.1530676095177.2ftrs8.1.1530676095177.1533350725169.2.9',
                # '_bfs': '1.3',
                # 'Mkt_UnionRecord': '%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1533350795097%7D%5D',
                # '_bfi': 'p1%3D101027%26p2%3D100101991%26v1%3D9%26v2%3D7',
                # '_jzqco': '%7C%7C%7C%7C1533350731192%7C1.824997734.1530676098057.1533350776875.1533350795104.1533350776875.1533350795104.undefined.0.0.9.9',
                # '__zpspc': '9.2.1533350731.1533350795.3%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%25E6%259C%25BA%25E7%25A5%25A8%7C%23',
                # 'appFloatCnt': '2'
            }
        )

    def parse(self, response):
        obj = json.loads(response.body.decode('gb2312'))
        print(obj['fis'])
        # for k in response.request.headers:
        #     print(k.decode()+":" + response.request.headers[k].decode())
