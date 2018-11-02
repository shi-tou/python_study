# scrapy
# -*- coding: UTF-8 -*-

import scrapy


class mingyanSpider(scrapy.Spider):
    name = "mingyan"
    start_urls = [
            'http://lab.scrapyd.cn/',
        ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            content = quote.css('span.text::text').extract_first()
            author = quote.xpath('span/small/text()').extract_first()
            f = open(author+'.txt', 'a+')
            f.write(content)
            f.write('\n')
            f.close

        #next_page = response.css('li.next a::attr("href")').extract_first()
        #if next_page is not None:
        #scrapy.Request(next_page, self.parse)
