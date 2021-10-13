# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


class DnsparserItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    rating = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    commentary = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Attrib_1 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Attrib_2 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Attrib_3 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Attrib_3 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Attrib_4 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    Attrib_5 = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
