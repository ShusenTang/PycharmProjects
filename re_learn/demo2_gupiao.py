# coding=utf-8
# 加上才能中文注释

# 淘宝搜索商品并比价
# 步骤一：利用东方财富网获取股票代码列表
# 步骤二：根据股票代码构造百度个股的网页地址获取个股信息
# 步骤三：结果存储至文件

import codecs

import sys
import os
import time

import requests
import re
from bs4 import BeautifulSoup
import traceback               # 调试用


def getHTMLText(url, code = 'utf-8'):
    #print 'getHTMLText...'
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()

        #r.encoding = r.apparent_encoding   #后者需要很长时间，所以可以手动获取直接赋值给前者以加快爬虫速度
        r.encoding = code
        #print r.text[:1000]

        return r.text
    except:
        return ''


def getStockList(lit,stockURL):

    #print 'getStockList...'

    html = getHTMLText(stockURL,'GB2312')   #东方财富网采用GB2312
    soup = BeautifulSoup(html,'html.parser')
    tag = soup.find_all('a')   #查看网页源代码知股票代码存放在a标签的herf中
    for i in tag:
        try:
            href = i.attrs['href']

            #print re.findall(r'[s][hz]\d{6}',href)[0]
            lit.append(re.findall(r'[s][hz]\d{6}',href)[0])#sh(或sz)+六个数字即股票代码
            #print lit[:100]
        except:
            continue      #解析异常时也能继续运行

def getStockInfo(lst,stockURL,filepath):

    #print 'getStockInfo...'

    count = 0


    for stock in lst:
        url = stockURL + stock + '.html'
        html = getHTMLText(url)   #百度采用默认的utf-8编码
        try:
            if html == '':    #若是空页面则跳过
                continue
            infoDict = {}
            soup = BeautifulSoup(html,'html.parser')
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})
            #print type(stockInfo)
            name = stockInfo.find_all(attrs = {'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})

            keylist = stockInfo.find_all('dt')
            valuelist = stockInfo.find_all('dd')
            for i in range(len(keylist)):
                key = keylist[i].text
                val = valuelist[i].text
                infoDict[key] = val  #向字典新增内容

            # file = open(filepath, 'a', encoding='utf8')  # 指定写入编码为utf8，否则写入中文会乱码
            # file.write(str(infoDict) + '\n')

            mystr = infoDict
            #print type(mystr)
            #print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
            for i in infoDict.keys():
                print i.decode('utf-8'),infoDict[i].decode('utf-8')

            #print str(infoDict).decode('utf-8') + '\n'



            # f = codecs.open(filepath, 'w')#, 'utf-8')
            #
            # f.write(str(infoDict).decode('utf-8') + '\n')
            # for i in list1:
            #     i = i + ' '
            #     f.write(i, )

            #f.close()

            # with open(filepath,'a') as f:
            #     #print str(infoDict)
            #     f.write(str(infoDict) + '\n')
            #
            #     count+=1
            #     percent = count*100 / len(lst)
            #     print 'complete percent:' + str(percent) + '%',
            #     sys.stdout.write("\r")
            #     #time.sleep(0.1)
            #     #print('\r当前速度：{:.2f}%'.format(count*100/len(lst)))



        except:
            count += 1
            percent = count * 100 / len(lst)
            print 'complete percent:' + str(percent) + '%',
            sys.stdout.write("\r")
            #time.sleep(0.1)
            #print('\r当前速度：{:.2f}%'.format(count * 100 / len(lst)))
            traceback.print_exc()   #出错时打印错误信息
            continue



if __name__ == '__main__':
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_path = '/Users/tang/PycharmProjects/re_learn/BaiduStockInfo.txt'
    slist = []
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_path)
    #os.remove(output_path)
