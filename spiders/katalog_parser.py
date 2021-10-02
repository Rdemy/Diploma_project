import scrapy
from dnsparser.items import DnsparserItem


class EKatalogPartsSpider(scrapy.Spider):
    name = 'parts'
    start_urls = ['https://www.kns.ru/catalog/komplektuyuschie/']

    def parse(self, response):
        item = DnsparserItem()
        item['product_name'] = response.xpath('//a[@class="name d-block"]//span/text()').get()
        item['product_price'] = response.xpath('//span[@class="price my-1"]/text()').get()
        item['product_price'] = [price.replace('\xa0', '') for price in item['product_price']]
        yield item