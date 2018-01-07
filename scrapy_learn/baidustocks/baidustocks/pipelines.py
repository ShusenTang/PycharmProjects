# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class BaidustocksPipeline(object):
#     def process_item(self, item, spider):
#         return item

class BaidustocksInfoPipeline(object):
    def open_spider(self,spider):          # 爬虫被调用时对应的pipeline启动的方法
        self.f = open('BaiduStocksInfo.txt','w')  #打开爬虫时要建立文件

    def close_spider(self,spider):         # 爬虫结束时对应的pipeline的方法
        self.f.close()                     # 关闭爬虫时文件也应该被关闭

    def process_item(self, item, spider):  # 对每一个item处理的方法
        try:
            line = str(dict(item)) + '\n'
            self.f.write(line)

        except:
            pass

        return item