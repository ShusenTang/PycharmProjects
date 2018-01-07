# -*- coding: utf-8 -*-
import scrapy
import re

from ..items import BaidustocksItem


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    start_urls = ['http://quote.eastmoney.com/stocklist.html']



    def parse(self, response):
        for href in response.css('a::attr(href)').extract():  # 用css selector解析所有a标签下属性为href的内容
            try:
                stock = re.findall(r"[s][hz]\d{6}",href)[0]   # 获取股票代码
                url = "http://gupiao.baidu.com/stock/" + stock + ".html"
                print '---------------URL---------',url,'----------URL------------'

                yield scrapy.Request(url,callback=self.parse_stock)
                #yield为生成器关键字，callback=self.parse_stock表示用parse_stock函数处理这个url内容

            except:
                continue

    def parse_stock(self,response):
        # 这个函数必须返回字典型(以给pipelines处理)，所以先定义一个字典
        infoDict = {}
        stockinfo = response.css('.stock-bets')
        test = response.css('script::text').extract()[0]
        # stockinfo = response.xpath('/div[@class="stock-info"]/div/text()').extract()
        print '0000000000000000000000',test,'0000000000000000000'
        # stockinfo = response.css('a[href*=image]::attr(href)').extract()
        print '++++++++++++++++',stockinfo.css(".bets-name").extract(),'++++++++++++++++++'
        name = stockinfo.css(".bets-name").extract()[0]
        #name = response.xpath('//div[@class="stock-info"]/div/h1/a/text()').extract_first()
        keylist = stockinfo.css("dt").extract()
        valuelist = stockinfo.css("dd").extract()
        stockinfo = response.css('.stock-bets')


        print '---------------------------',name,keylist[1:3],valuelist[1:3],'-------------'
        for i in range(len(keylist)):
            key = re.findall(r'>.*</dt>',keylist[i])[0][1:-5]
            try:
                value = re.findall(r'\d+\.?.*</dd>', valuelist[i])[0][1:-5]
            except:
                value = '--'

            infoDict[key] = value

        infoDict.update(
            {
                '股票名称':re.findall('\s.*\(',name)[0].split()[0] + \
                re.findall('\>.*\<',name)[0][1:-1]
            }
        )

        yield infoDict    # 送给pipeline


