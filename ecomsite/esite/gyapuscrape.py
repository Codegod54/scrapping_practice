import django.db
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.edge.service import Service


class GyapuscraperSpider(Spider):
    name = "gyapuscrape"
    allowed_domains = ["gyapu.com"]
    start_urls = ["https://www.gyapu.com/category/laptops1"]

    def __init__(self):
 
        self.driver = webdriver.Edge(service=self.service)

    def parse(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)

       
        product_elements = sel.xpath('div.categoryRightTop flex flex-wrap")]')

        for product in product_elements:
            
            image_url = product.xpath('div.fslink relative::attr(href)').get()
            product_name = product.xpath('div.fsdet_title text-secondary text-md sm:text-sm text-center hover:text-primary line-clamp::text').get()
            product_price = product.xpath('div.price text__price text-center text-lg  font-bold::text').get() 
            print('pro price: ', product_price)

        yield {
                'product_name': product_name,
                'product_price': product_price,
                'image_url': image_url,

            }
        
