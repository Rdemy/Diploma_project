from itemloaders import processors
import scrapy
from scrapy import selector
from dnsparser.items import DnsparserItem
from scrapy.loader import ItemLoader


class ProceccorsSpider(scrapy.Spider):
    name = 'procers'
    start_urls = ['https://www.kns.ru/catalog/komplektuyuschie/']
    pages_count = 1

    def start_requests(self):
        for page in range(1, 1 + self.pages_count):
            url = f'https://www.kns.ru/catalog/komplektuyuschie/protsessory/page{page}/'
            yield scrapy.Request(url, callback=self.parse_pages)

    def parse_pages(self, response):
        for href in response.xpath('//a[@class = "name d-block"]//@href').getall():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.info_parse)

    def info_parse(self, response):
        info_link = response.xpath('//*[@class = "cont bg-white p-1"]')
        for proccesors in info_link:
            l = ItemLoader(item=DnsparserItem(), selector=proccesors)
            l.add_xpath('name', '//h1[@itemprop = "name"]')
            l.add_xpath('price', '//span[@class = "price-val"]')
            l.add_xpath('rating', '//div[@class = "aggregate-rating"]//meta[1]/@content')
            l.add_xpath('commentary', '//div[@class = "aggregate-rating"]//meta[2]/@content')
            l.add_xpath('cores', '//div[@data-id = "1416601096"]')
            l.add_xpath('frequency', '//div[@data-id = "1416601099"]')
            l.add_xpath('waranty_procs', '//div[@data-id = "1416604950"]')
            l.add_xpath('proc_memory_type', '//div[@data-id = "1416605706"]')
            l.add_xpath('tech_process', '//div[@data-id = "1416601097"]')
            yield l.load_item()


class BoardSpider(scrapy.Spider):
    name = 'motherboards'
    start_urls = ['https://www.kns.ru/catalog/komplektuyuschie/']
    pages_count = 1

    def start_requests(self):
        for page in range(1, 1 + self.pages_count):
            url = f'https://www.kns.ru/catalog/komplektuyuschie/materinskie-platy/page{page}/'
            yield scrapy.Request(url, callback=self.parse_pages)

    def parse_pages(self, response):
        for href in response.xpath('//a[@class = "name d-block"]//@href').getall():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.info_parse)

    def info_parse(self, response):
        info_link = response.xpath('//*[@class = "cont bg-white p-1"]')
        for proccesors in info_link:
            l = ItemLoader(item=DnsparserItem(), selector=proccesors)
            l.add_xpath('name', '//h1[@itemprop = "name"]')
            l.add_xpath('price', '//span[@class = "price-val"]')
            l.add_xpath('rating', '//div[@class = "aggregate-rating"]//meta[1]/@content')
            l.add_xpath('commentary', '//div[@class = "aggregate-rating"]//meta[2]/@content')
            l.add_xpath('socket', '//div[@data-id = "1417701259"]')
            l.add_xpath('chipset', '//div[@data-id = "1417701267"]')
            l.add_xpath('memory_board', '//div[@data-id = "1417701270"]')
            l.add_xpath('memory_slots', '//div[@data-id = "1417701274"]')
            l.add_xpath('memory_value', '//div[@data-id = "1417701278"]')
            l.add_xpath('waranty_board', '//div[@data-id = "1417704950"]')
            yield l.load_item()


class VideoSpider(scrapy.Spider):
    name = 'videocards'
    start_urls = ['https://www.kns.ru/catalog/komplektuyuschie/']
    pages_count = 1

    def start_requests(self):
        for page in range(1, 1 + self.pages_count):
            url = f'https://www.kns.ru/catalog/komplektuyuschie/videokarty/page{page}/'
            yield scrapy.Request(url, callback=self.parse_pages)

    def parse_pages(self, response):
        for href in response.xpath('//a[@class = "name d-block"]//@href').getall():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.info_parse)

    def info_parse(self, response):
        info_link = response.xpath('//*[@class = "cont bg-white p-1"]')
        for proccesors in info_link:
            l = ItemLoader(item=DnsparserItem(), selector=proccesors)
            l.add_xpath('name', '//h1[@itemprop = "name"]')
            l.add_xpath('price', '//span[@class = "price-val"]')
            l.add_xpath('rating', '//div[@class = "aggregate-rating"]//meta[1]/@content')
            l.add_xpath('commentary', '//div[@class = "aggregate-rating"]//meta[2]/@content')
            l.add_xpath('brand', '//div[@data-id = "1421001146"]')
            l.add_xpath('video_memory_type', '//div[@data-id = "1421001156"]')
            l.add_xpath('video_memory_value', '//div[@data-id = "1421001155"]')
            l.add_xpath('dram', '//div[@data-id = "1421001157"]')
            l.add_xpath('max_video_resolution', '//div[@data-id = "1421001152"]')
            l.add_xpath('waranty_video', '//div[@data-id = "1416704950"]')
            l.add_xpath('freq_video', '//div[@data-id = "1421001158"]')
            yield l.load_item()


class RAMSpider(scrapy.Spider):
    name = 'RAM'
    start_urls = ['https://www.kns.ru/catalog/komplektuyuschie/']
    pages_count = 1

    def start_requests(self):
        for page in range(1, 1 + self.pages_count):
            url = f'https://www.kns.ru/catalog/komplektuyuschie/pamyat/page{page}/'
            yield scrapy.Request(url, callback=self.parse_pages)

    def parse_pages(self, response):
        for href in response.xpath('//a[@class = "name d-block"]//@href').getall():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.info_parse)

    def info_parse(self, response):
        info_link = response.xpath('//*[@class = "cont bg-white p-1"]')
        for proccesors in info_link:
            l = ItemLoader(item=DnsparserItem(), selector=proccesors)
            l.add_xpath('name', '//h1[@itemprop = "name"]')
            l.add_xpath('price', '//span[@class = "price-val"]')
            l.add_xpath('rating', '//div[@class = "aggregate-rating"]//meta[1]/@content')
            l.add_xpath('commentary', '//div[@class = "aggregate-rating"]//meta[2]/@content')
            l.add_xpath('RAM_memory_type', '//div[@data-id = "1418601123"]')
            l.add_xpath('RAM_memory_value', '//div[@data-id = "1418605199"]')
            l.add_xpath('waranty_RAM', '//div[@data-id = "1418604950"]')
            yield l.load_item()


class HDDSpider(scrapy.Spider):
    name = 'HDD'
    start_urls = ['https://www.kns.ru/catalog/komplektuyuschie/']
    pages_count = 1

    def start_requests(self):
        for page in range(1, 1 + self.pages_count):
            url = f'https://www.kns.ru/catalog/komplektuyuschie/zhestkie-diski/page{page}/'
            yield scrapy.Request(url, callback=self.parse_pages)

    def parse_pages(self, response):
        for href in response.xpath('//a[@class = "name d-block"]//@href').getall():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.info_parse)

    def info_parse(self, response):
        info_link = response.xpath('//*[@class = "cont bg-white p-1"]')
        for proccesors in info_link:
            l = ItemLoader(item=DnsparserItem(), selector=proccesors)
            l.add_xpath('name', '//h1[@itemprop = "name"]')
            l.add_xpath('price', '//span[@class = "price-val"]')
            l.add_xpath('rating', '//div[@class = "aggregate-rating"]//meta[1]/@content')
            l.add_xpath('commentary', '//div[@class = "aggregate-rating"]//meta[2]/@content')
            l.add_xpath('HDD_model', '//div[@data-id = "1419304831"]')
            l.add_xpath('speed', '//div[@data-id = "1419301244"]')
            l.add_xpath('HDD_memory_value', '//div[@data-id = "1419301233"]')
            l.add_xpath('waranty_HDD', '//div[@data-id = "1416704950"]')
            yield l.load_item()


class SDDSpider(scrapy.Spider):
    name = 'SSD'
    start_urls = ['https://www.kns.ru/catalog/komplektuyuschie/']
    pages_count = 1

    def start_requests(self):
        for page in range(1, 1 + self.pages_count):
            url = f'https://www.kns.ru/catalog/komplektuyuschie/ssd/page{page}/'
            yield scrapy.Request(url, callback=self.parse_pages)

    def parse_pages(self, response):
        for href in response.xpath('//a[@class = "name d-block"]//@href').getall():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.info_parse)

    def info_parse(self, response):
        info_link = response.xpath('//*[@class = "cont bg-white p-1"]')
        for proccesors in info_link:
            l = ItemLoader(item=DnsparserItem(), selector=proccesors)
            l.add_xpath('name', '//h1[@itemprop = "name"]')
            l.add_xpath('price', '//span[@class = "price-val"]')
            l.add_xpath('rating', '//div[@class = "aggregate-rating"]//meta[1]/@content')
            l.add_xpath('commentary', '//div[@class = "aggregate-rating"]//meta[2]/@content')
            l.add_xpath('SDD_model', '//div[@data-id = "44622004831"]')
            l.add_xpath('SSD_speed', '//div[@data-id = "44622001336"]')
            l.add_xpath('SSD_memory_value', '//div[@data-id = "44622001233"]')
            l.add_xpath('waranty_SSD', '//div[@data-id = "1416704950"]')
            yield l.load_item()