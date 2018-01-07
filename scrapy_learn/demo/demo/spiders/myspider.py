# -*- coding: utf-8 -*-

import scrapy
import re
# from demo.items import DemoItem
from ..items import DemoItem

#  scrapy crawl myspider -o stocksinfo.csv


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    #  allowed_domains = ['python123.io']
    # start_urls = ['https://python123.io/ws/demo.html']     # 启动时进行爬取的url列表,后续的URL则从初始的URL获取到的数据中提取

    start_urls = ['http://quote.eastmoney.com/stocklist.html']


    def parse(self, response):
        for href in response.css('a::attr(href)').extract():  # 用css selector解析所有a标签下属性为href的内容
            try:
                stock = re.findall(r"[s][hz]\d{6}",href)[0]   # 获取股票代码
                url = "http://gupiao.baidu.com/stock/" + stock + ".html"
                #print '---------------URL---------',url,'----------URL------------'

                yield scrapy.Request(url,callback=self.parse_stock)
                #yield为生成器关键字，callback=self.parse_stock表示用parse_stock函数处理这个url内容

            except:
                continue


    def parse_stock(self, response):
        try:
            infodict = {}
            infodict['股票名'] = re.findall('\\n.+\s',response.xpath('//h1/a/text()').extract()[0])[0].strip()  #strip去掉空格
            keylist = response.xpath('//*[@class="bets-content"]/div/dl/dt/text()').extract()
            valuelist = response.xpath('//*[@class="bets-content"]/div/dl/dd/text()').extract()

            for i in range(len(keylist)):
                key = keylist[i]
                value = valuelist[i]
                infodict[key] = value
            yield infodict
        except:
            pass



