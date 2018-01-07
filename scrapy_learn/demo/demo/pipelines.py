# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DemoPipeline(object):
    # def process_item(self, item, spider):
    #     for key,value in item.items():
    #         print key,value

        #print '2222222222222222222222', item
        #print '2222222222222222222222', item[u'最低']
        #print '2222222222222222222222', item[u'金开']
    def open_spider(self, spider):  # 爬虫被调用时对应的pipeline启动的方法
        self.f = open('info.txt', 'w')  # 打开爬虫时要建立文件

    def close_spider(self, spider):  # 爬虫结束时对应的pipeline的方法
        self.f.close()  # 关闭爬虫时文件也应该被关闭

    def process_item(self, item, spider):  # 对每一个item处理的方法
        print '股票名:',item['股票名'],' ',
        try:
            for key,value in item.items():
                if key != '股票名':
                    print key,':',value,' ',
            print '\n'

        except:
            pass

        return item
