# coding=utf-8
# 加上第一行才能中文注释

import requests
from bs4 import BeautifulSoup
import json


# 将获取评论数封装成函数

def getCommentCounts(newsurl):
    news_id = newsurl.split('/')[-1].strip('.shtml').strip('doc-i')  # split('/')是以/为分隔符将字符串切割成不同部分形成list

    comment_BlankUrl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=sh&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'#挖掉了newsid，用{}代替
    commenturl = comment_BlankUrl.format(news_id)#将newsid填进来形成完整的评论网址
    comment_res = requests.get(commenturl)
    need_tobe_delete = comment_res.text.split('{')[0]#想删除的部分'var loader...='
    #print'1',(comment_res.text.strip(need_tobe_delete))
    # try:
    jd = json.loads(comment_res.text.strip(need_tobe_delete))#删除'var loader...=',只保留{...} ，即形成字典
    #print jd

    # 有时候channel可能是gn,会导致错误
    if jd['result']['status']['code']!=0:
        commenturl = commenturl.replace('channel=sh','channel=gn')
        comment_res = requests.get(commenturl)
        need_tobe_delete = comment_res.text.split('{')[0]  # 想删除的部分'var loader...='
        #print(comment_res.text.strip(need_tobe_delete))
        jd = json.loads(comment_res.text.strip(need_tobe_delete))
        #print jd
        if jd['result']['status']['code'] != 0:
            commenturl = commenturl.replace('channel=gn', 'channel=gj')
            comment_res = requests.get(commenturl)
            need_tobe_delete = comment_res.text.split('{')[0]  # 想删除的部分'var loader...='
            jd = json.loads(comment_res.text.strip(need_tobe_delete))
            #print jd
    # except:
    #     print jd

    if jd['result']['status']['code'] == 0:
        return jd['result']['count']['total']
    else:
        return False


res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

for news in soup.select('.news-item'):
    if len(news.select('h2')) > 0:
        h2 = news.select('h2')[0].text
        time = news.select('.time')[0].text  # 注意time前面的'.'
        a = news.select('a')[0]['href']
        print h2, time, a, '评论数为：', getCommentCounts(a)
