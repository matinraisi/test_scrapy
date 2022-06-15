import scrapy 

class testSpider(scrapy.Spider):
    name = "TestSpider"
    start_urls = ['https://www.tasnimnews.com/fa/news/1401/03/24/2728494/']

    def parse(self,response):
      print(response.css(
        'div.p::text'
      ).extract())