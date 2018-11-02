# scrapy  执行scrapy crawl taobao
# -*- coding: UTF-8 -*-

import scrapy


class taobaoSpider(scrapy.Spider):  # 需要继承scrapy.Spider类
    name = "taobao"  # 定义蜘蛛名
    start_urls = [
            'http://lab.scrapyd.cn'
        ]

    def parse(self, response):
        '''
        start_requests已经爬取到页面，那如何提取我们想要的内容呢？那就可以在这个方法里面定义。
        这里的话，并木有定义，只是简单的把页面做了一个保存，并没有涉及提取我们想要的数据，后面会慢慢说到
        也就是用xpath、正则、或是css进行相应提取，这个例子就是让你看看scrapy运行的流程：
        1、定义链接；
        2、通过链接爬取（下载）页面；
        3、定义规则，然后提取数据；
        就是这么个流程，似不似很简单呀？
        '''
        taobao = response.css('div.quote')

        for v in taobao:  # 循环获取每一条名言里面的：名言内容、作者、标签

            text = v.css('.text::text').extract_first()  # 提取名言
            autor = v.css('.author::text').extract_first()  # 提取作者
            tags = v.css('.tags .tag::text').extract()  # 提取标签
            tags = ','.join(tags)  # 数组转换为字符串
            # 接下来，进行保存
            fileName = '%s-语录.txt' % autor  # 爬取的内容存入文件，文件名为：作者-语录.txt
            f = open(fileName, "a+")  # 追加写入文件
            f.write(text)  # 写入名言内容
            f.write('\n')  # 换行
            f.write('标签：'+tags)  # 写入标签
            f.write('\n------------------------------------\n')  # 换行
            f.close()  # 关闭文件操作
        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, self.parse)