# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FlightsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CitiesItem(scrapy.Item):
    name = scrapy.Field()
    code = scrapy.Field()
