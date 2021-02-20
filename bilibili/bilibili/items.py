# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:

    title = scrapy.Field()
    author = scrapy.Field()
    like_count = scrapy.Field()
    coin_count = scrapy.Field()
    collect_count = scrapy.Field()
    view_count = scrapy.Field()
    dm_count = scrapy.Field()
    bv = scrapy.Field()
    dm = scrapy.Field()
