# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy import  Item ,Field
class ProductItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    table = 'data2'
    序号 = Field()
    基金代码 = Field()
    基金简称 = Field()
    日期 = Field()
    单位净值 = Field()
    累计净值 = Field()
    日增长率 = Field()
    近1周 = Field()
    近1月 = Field()
    近3月 = Field()
    近6月 = Field()
    近1年 = Field()
    近2年 = Field()
    近3年 = Field()
    今年来 = Field()
    成立来 = Field()

