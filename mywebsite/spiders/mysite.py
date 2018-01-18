import scrapy
from scrapy import Request
from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
# from tovantran.items import TovantranItem

class MySpider(scrapy.Spider):
        post=0
        def __init__(self, post=None):  #post empty state
        # def __init__(self, post): 
          super(MySpider, self).__init__(post)
          # self.post = 0
        name = "tovantran"
        allowed_domains = ["tovantran.com"]
        start_urls = [
            "http://tovantran.com/blog"    ]
       
        def parse(self, response):
            titles = response.xpath('//h2//a').extract()
            dates = response.xpath('//h4/text()').extract()
            items_date = []
            items_title = []
            for date in dates: 
              items_date.append(date)
              # yield (date)
            for title in titles:
                print(spide.post)
                spide.post += 1
                date = items_date.pop(0)
                yield {'Post': '{:>3}'.format(spide.post), 'Date': '{:>25}'.format(date),  'Title':title }
            relative_next_url = response.xpath('//a[@class="next"]/@href').extract_first()  # next page start over 
            absolute_next_url = response.urljoin(relative_next_url)
            yield Request(absolute_next_url, callback=self.parse)  # callback for next page does the same goes parse

spide = MySpider(0) 
print(spide.post)
  