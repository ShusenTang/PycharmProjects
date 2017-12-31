#coding:utf-8

'''获取Bing主页图片并存储，配合Automator可以在MacOS上实现一键将Bing主页图片作为桌面壁纸'''

import requests
import re
import os      # 要进行有关文件的操作
import time    # 取得今日日期以建立文件名

def Create_file_folder(path):
    if os.path.exists(path)==False:
        print 'pictures不存在，正在新建文件夹。。。。。。'
        try:
            os.mkdir(path)
            print '文件夹建立成功，继续运行程序。。。。。。'
        except:
            print "文件夹建立失败！！！"

def GetPicURL(Bing_URL):
    h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2704.63 Safari/537.36'}  # 浏览器伪装
    html = requests.get(Bing_URL,headers = h).text
    tmp = re.findall("g_img={url:(.*?)}", html)[0]     # 正则模式匹配这里没搞好，故下面还要分割一下。。。
    ls = re.split(r'"',tmp)
    return Bing_URL+ls[1]

def Get_Pic(Pic_URL,folder_path):
    pic = requests.get(Pic_URL)
    pic_name = "/" + time.strftime('%Y_%m_%d', time.localtime(time.time())) + ".jpg"
    pic_path = folder_path+pic_name
    if os.path.exists(pic_path):
        print '已存在今日图片！'
    else:
        if len(os.listdir(folder_path)) > 30:     #如果文件夹里有很多之前的图片，可将其清空
            for jpg in os.listdir(folder_path):
                jpg_path = os.path.join(folder_path,jpg) #取图片路径
                os.remove(jpg_path)

        print '正在存储今日图片。。。。'
        try:
            fp = open(pic_path, 'wb')
            fp.write(pic.content)
            fp.close()
            print '成功获取今日图片，图片存放至',pic_path
        except:
            print "存储失败！！！"

if __name__ == '__main__':
    BingURL = "https://cn.bing.com"
    pic_file_folder_path = r'/Users/tang/PycharmProjects/get_bing_pic/pictures'
    Create_file_folder(pic_file_folder_path)        # 必要时创建文件夹
    pic_url = ""
    try:
        pic_url = GetPicURL(BingURL)                # 获取今天Bing图片的地址
        Get_Pic(pic_url,pic_file_folder_path)       # 获得图片并存储
    except:                                         # 如果网络异常的话什么都不做
        pass



