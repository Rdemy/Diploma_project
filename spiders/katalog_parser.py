import scrapy


class EKatalogPartsSpider(scrapy.Spider):
    name = 'parts'
    start_urls = ['https://www.kns.ru/catalog/komplektuyuschie/']

    def parse(self, response):
        details = response.xpath('//*[@class = "goods-list-item mx-auto"]')
        for category in details:
            yield {
                    'name': category.xpath('./*[@class="position-relative my-1 name-cont pr-xl-0"]//span/text()').get(),
                    'price': category.xpath('./*[@class="block-price"]//span/text()').get().replace('\xa0',''),
                    'description': category.xpath('./*[@class = "position-relative my-1 name-cont pr-xl-0"]//div/div/text()').get(),
                    'rating': category.xpath('//div[@class="col-12 col-sm-6 text-md-right block-info"]//div//meta[1]/@content').get()
            }
