#coding:utf-8

#步骤一：建立一个scrapy爬虫工程：在shell中进入想建立工程位置的文件夹再执行scrapy startproject 工程名(如demo1)
#步骤二：在工程中产生一个scrapy爬虫：在shell中进入上一步创建的demo1文件夹执行scrapy genspider 爬虫名(如demo) 域名(如python123.io)
#步骤三：编写spider使满足我们的需求：修改上一步产生在spiders目录下的demo.py代码
#步骤五：编写pipeline以处理spider所提取的信息
#步骤五：运行爬虫:在shell执行scrapy crawl 爬虫名(demo)
#
