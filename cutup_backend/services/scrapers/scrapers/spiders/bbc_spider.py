import scrapy

class BbcSpider(scrapy.Spider):
    name = "BBC"
    start_urls = ['http://www.bbc.com/news']

    def parse(self, response):
        for title in response.css('div.gel-layout__item'):
            yield {
                'headline': title.css('h3::text').extract_first()
            }
