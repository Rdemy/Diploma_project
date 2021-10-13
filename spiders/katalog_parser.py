from itemloaders import processors
import scrapy
from scrapy import selector
from dnsparser.items import DnsparserItem
from scrapy.loader import ItemLoader


class EKatalogPartsSpider(scrapy.Spider):
    name = 'parts'
    start_urls = ['https://www.kns.ru/catalog/komplektuyuschie/protsessory/']

    def parse(self, response):
        for category in response.xpath('//a[@class = "name d-block"]//@href'):
            yield response.follow(category, callback=self.info_parse)

        for pages in response.xpath('//*[@class="page-link"]//@href')[1]:
            yield response.follow(pages, callback=self.parse)

    def info_parse(self, response):
        info_link = response.xpath('//*[@class = "cont bg-white p-1"]')
        for proccesors in info_link:
            l = ItemLoader(item=DnsparserItem(), selector=proccesors)
            l.add_xpath('name', '//h1[@itemprop = "name"]')
            l.add_xpath('price', '//span[@class = "price-val"]')
            l.add_xpath('rating', '//div[@class = "aggregate-rating"]//meta[1]/@content')
            l.add_xpath('commentary', '//div[@class = "aggregate-rating"]//meta[2]/@content')
            l.add_xpath('Attrib_1', '//div[@data-id = "1416601096"]')
            l.add_xpath('Attrib_2', '//div[@data-id = "1416601099"]')
            l.add_xpath('Attrib_3', '//div[@data-id = "1416604950"]')
            l.add_xpath('Attrib_4', '//div[@data-id = "1416605706"]')
            l.add_xpath('Attrib_5', '//div[@data-id = "1416601097"]')
            yield l.load_item()

