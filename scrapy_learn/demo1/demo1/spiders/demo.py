# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

class DemoSpider(scrapy.Spider):              # DemoSpider继承了scrapy.Spider
    name = 'demo'
    # allowed_domains = ['python123.io']      # 域名，代表只能爬取这个域名以下的内容。这行其实不需要，可注释掉
    start_urls = ['https://python123.io/ws/demo.html']     # 启动时进行爬取的url列表,后续的URL则从初始的URL获取到的数据中提取



    # 被调用时，每个初始URL完成下载后生成的Response对象将会作为唯一的参数传递给该函数。
    # 该方法负责解析返回的数据(response data)
    # 并提取数据(生成item，字典)以及生成需要进一步处理的URL的Request对象
    def parse(self, response):
        file_name = response.url.split('/')[-1]  # 文件名
        fp = open(file_name, 'wb')
        fp.write(response.body)
        fp.close()
        print '-----------------------------begin-----------------------------'
        print '包体：',response.body
        print '包头：',response.headers

        print '选择HTML文档中<head>标签内的 <title> 元素：',response.xpath('/html/head/title')
        print '序列化该节点为unicode字符串并返回list：',response.xpath('/html/head/title').extract()
        print '输出上面元素的文本：',response.xpath('/html/head/title/text()').extract()
        print type(response.xpath('/html/head/title/text()'))
        print '传入正则表达式对数据进行提取，返回unicode字符串list',\
            response.xpath('/html/head/title/text()').re('(.+)')
        print '选择所有的 <title> 元素:', response.xpath('//title')  # //代表从根目录
        print '选择所有具有 class="course" 属性的p元素:', response.xpath('//p[@class="course"]')


        #####################提取数据################

        #提取里面的两个url,查看网页源代码发现两个url都在a的href属性下
        urls = response.xpath('//a/@href').extract()  # //代表从根目录
        for url in urls:
            print url
        print response.xpath('//a/text()').extract()[0]  # 两个网站标题


        for url in urls:
            try:
                yield scrapy.Request(url, callback=self.parse_url)
                    # yield为生成器关键字，callback=self.parse_url表示用parse_url函数处理这个url内容
            except:
                continue



    #在shell中运行scrapy runspider demo.py -o abc.csv就会将以下数据保存到abc.csv中(csv也可换成json和xml)
    def parse_url(self, response):
        infodic = {}
        for i in response.xpath('/html/head'):
            infodic['title'] = i.xpath('title/text()').extract()[0]
            #infodic['简介'] = i.xpath('//*[@id="j-rectxt2"]/text()').extract()
            print '###############################',infodic['title']


        yield infodic



        print '-----------------------------done!-----------------------------'
