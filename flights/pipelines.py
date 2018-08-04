# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FlightsPipeline(object):
    def process_item(self, item, spider):
        return item


class CleanPipeline(object):
    rules = {
        '&nbsp;': ' ',
        '  ': ' '
    }

    def process_item(self, item, spider):
        for field in item.fields:
            item[field] = self.clean(item[field])
        return item

    def clean(self, text):
        result = text
        for key in self.rules:
            result = result.replace(key, self.rules[key])
        return result.strip()
