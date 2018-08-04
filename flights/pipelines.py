# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from scrapy.exporters import JsonLinesItemExporter
import os


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
            if type(item[field]) == str:
                item[field] = self.clean(item[field])
        return item

    def clean(self, text):
        result = text
        for key in self.rules:
            result = result.replace(key, self.rules[key])
        return result.strip()


class JsonExportPipeline(object):

    exporters = {}
    outputs = 'outputs'

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        if not os.path.isdir(self.outputs):
            os.mkdir(self.outputs)
        path = os.path.join(self.outputs, f'{spider.name}.json')
        if os.path.isfile(path):
            os.unlink(path)
        file = open(path, 'a+b')
        self.exporters[spider.name] = JsonLinesItemExporter(file)
        self.exporters[spider.name].start_exporting()

    def spider_closed(self, spider):
        self.exporters[spider.name].finish_exporting()
        self.exporters[spider.name].file.close()

    def process_item(self, item, spider):
        self.exporters[spider.name].export_item(item)
        return item
