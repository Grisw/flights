# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FlightsItem(scrapy.Item):
    airline = scrapy.Field()
    flight = scrapy.Field()
    departure = scrapy.Field()
    arrival = scrapy.Field()
    departure_time = scrapy.Field()
    arrival_time = scrapy.Field()
    price = scrapy.Field()
    crawl_time = scrapy.Field()


class CitiesItem(scrapy.Item):
    code = scrapy.Field()
    city = scrapy.Field()
    airport = scrapy.Field()


class AirlinesItem(scrapy.Item):
    code = scrapy.Field()
    name = scrapy.Field()
