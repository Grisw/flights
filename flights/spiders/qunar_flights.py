# -*- coding: utf-8 -*-
import scrapy
import json


class QunarFlightsSpider(scrapy.Spider):
    name = 'qunar_flights'
    start_url = 'https://flight.qunar.com/touch/api/domestic/wbdflightlist'

    def start_requests(self):
        departure_city = '上海'
        arrival_city = '北京'
        departure_date = '2018-07-20'

        url = '{}?departureCity={}&arrivalCity={}&departureDate={}'.format(self.start_url, departure_city,
                                                                           arrival_city, departure_date)
        yield scrapy.Request(
            url,
            headers={
                'cookie': 'QN99=7358; QN300=auto_4e0d874a; QN1=O5cv5VsY7IiyzpJMFNWwAg==; QunarGlobal=10.86.213.148_-1b5fa719_163d94e4317_97b|1528360072986; QN601=d232a276138ae45c598ef5ef6fb9dd55; _i=RBTKSdOklzHx5e9T61W6YF9oS2bx; QN48=tc_920011d290b12016_163d95c0177_30d5; QN73=3175-3178; __utma=183398822.2130918933.1528360123.1528360123.1528360123.1; __utmz=183398822.1528360123.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _jzqa=1.708127243630048300.1528360127.1528360127.1528360127.1; _jzqx=1.1528360127.1528360127.1.jzqsr=hotel%2Equnar%2Ecom|jzqct=/city/hongkong_city/.-; Qs_lvt_55613=1528360550; Hm_lvt_8fa710fe238aadb83847578e333d4309=1528360551; Qs_pv_55613=4274381182899892700%2C2085059948103910000%2C3699914886974703000%2C4409085049595466000%2C4045826998020648000; QN205=auto_4e0d874a; QN277=auto_4e0d874a; QN170=120.43.40.144_33768f_0_kedYNBE008ISEW%2Fw1O9PbA%2F1pZS%2BBwxE2lAtuZBnBvc%3D; SC1=c02cedae9602f1efdd713510958f8d90; SC18=; _RSG=FFaqxQlNGF9cQFKaUGSen8; _RDG=28fc90eb234f1729ea1c1491b0bdb73881; _RGUID=93d05ef6-bbd2-43cf-8c68-7107a450f6a6; Hm_lvt_75154a8409c0f82ecd97d538ff0ab3f3=1528360074,1530675958,1530680085; QN243=1; csrfToken=wNJuIj88K8Zl8fBY4A6egqsoKsbPMo2N; QN269=19CD55E17F3D11E89AD9FA163EF78B12; F235=1531139611461; _RF1=120.43.37.7; QN621=1490067914133%3DDEFAULT%26fr%3Dqunarindex; _vi=2oYrTTBtrtNgySehwkBwh3EPOPF9eGe4sTGlL6IaIW6eUyxSlPdMn4lEpb_6YBnNpH-3VtPJ0e5Nzql4wShOhGqsOC7MegaPiydHaBwLSnx2pSSvxso1wDp-NmBXLAqJwgw-gIdlJxVW6sBqKIYsqk_16A1Skv-GVicKTdfVt0bx; QN667=B; QN668=51%2C55%2C53%2C51%2C51%2C54%2C54%2C53%2C50%2C50%2C51%2C52%2C59',
                '2ff795': 'b0b60aed049c7ba9c44f828e765b15a28178f494'
            },
            meta={'dont_cache': True},
            dont_filter=True
        )

    def parse(self, response):
        obj = json.loads(response.body.decode())
        if obj['code'] != 0:
            for i in self.start_requests():
                yield i
            return
        print(obj['data']['abt'])
        # for k in response.request.headers:
        #     print(k.decode()+":" + response.request.headers[k].decode())
