# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


class DnsparserItem(scrapy.Item):
# Basic attributes
    name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    rating = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    commentary = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())

# Proceccors attributes
    cores = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    frequency = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    waranty_procs = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    proc_memory_type = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    tech_process = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())

# Motherboard attributes
    socket = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    chipset = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    memory_board = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    memory_slots = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    memory_value = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    waranty_board = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())

# Videocard attributes
    brand = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    video_memory_type = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    video_memory_value = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    dram = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    max_video_resolution = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    waranty_video = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    freq_video = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())

# RAM attributes
    RAM_memory_type = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    RAM_memory_value = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    waranty_RAM = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())

# HDD attributes
    HDD_model = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    speed = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    HDD_memory_value = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    waranty_HDD = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())

# SSD attributes
    SDD_model = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    SSD_speed = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    SSD_memory_value = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    waranty_SSD = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())