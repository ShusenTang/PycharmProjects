# coding=utf-8
# 加上第一行才能中文注释

import requests
from bs4 import BeautifulSoup
import datetime

res = requests.get('http://news.sina.com.cn/o/2017-03-01/doc-ifyazwha3453369.shtml')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')

#抓取文章标题
print soup.select('#artibodyTitle')[0].text

#时间和来源
#print soup.select('.time-source')[0].text #这一句将会把时间和来源一起取出，设法将其分开
timesource = soup.select('.time-source')[0].contents[0].strip() #此时是unicode，设法改成时间格式，#strip()用于移除字符串头尾指定的字符（默认为空格)
timesource = timesource.encode('utf-8')#先转成utf-8
dt = datetime.datetime.strptime(timesource, '%Y年%m月%d日%H:%M')#utf-8转成时间格式
print dt
print soup.select('.time-source span span a')[0].text #.time-source span span a表示class=time-source下的span下的span下的a
# print soup.select('.time-source')[0].contents[1].text.strip()#也可以这样取得新闻来源

#正文
print len(soup.select('#artibody p'))#一共35个元素
# print soup.select('#artibody p')[34].text #最后一个是编辑
article = []
for paragraph in soup.select('#artibody p')[:-1]:#去掉最后的编辑
    # print paragraph.text.strip()#输出所有正文
    article.append(paragraph.text.strip())
contents = ' '.join(article)#将article中的各元素（段）用空格连接起来
print contents

#抓取编辑
# editor = soup.select('#artibody p')[34].text# 或者下面的方法
editor = soup.select('.article-editor')[0].text.encode('utf-8').strip('责任编辑：')
print editor

#抓取评论数和评论内容
# count = soup.select('#commentCount1')
# print count
#以上方法并不奏效
comment_res = requests.get('http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fycaafm4652808&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20')
#('http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=sh&newsid=comos-fyazwha3453369&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20')
print comment_res.text # 这是json
import json
need_tobe_delete = comment_res.text.split('{')[0]
jd = json.loads(comment_res.text.strip(need_tobe_delete))#想删除的部分'var loader...='
comment_count = jd['result']['count']['total']#删除'var loader...=',只保留{...} ，即形成字典
print comment_count
# for i in range(0,12):
#     print jd['result']['cmntlist'][i]['content']#输出加载在页面中的12条评论内容


# 获取新闻编号，这里是fyazwha3453369
newsurl = 'http://news.sina.com.cn/o/2017-03-01/doc-ifyazwha3453369.shtml'
news_id = newsurl.split('/')[-1].strip('.shtml').strip('doc-i') #split('/')是以/为分隔符将字符串切割成不同部分形成list
print news_id

#将获取评论数封装成函数
def getCommentCounts(newsurl):
    news_id = newsurl.split('/')[-1].strip('.shtml').strip('doc-i')  # split('/')是以/为分隔符将字符串切割成不同部分形成list

    comment_BlankUrl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=sh&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'#挖掉了newsid，用{}代替
    commenturl = comment_BlankUrl.format(news_id)#将newsid填进来形成完整的评论网址
    comment_res = requests.get(commenturl)
    need_tobe_delete = comment_res.text.split('{')[0]#想删除的部分'var loader...='
    jd = json.loads(comment_res.text.strip(need_tobe_delete))#删除'var loader...=',只保留{...} ，即形成字典

    # 有时候channel可能是gn,会导致错误
    if jd['result']['status']['code']!=0 :
        commenturl = commenturl.replace('channel=sh','channel=gn')
        comment_res = requests.get(commenturl)
        need_tobe_delete = comment_res.text.split('{')[0]  # 想删除的部分'var loader...='
        jd = json.loads(comment_res.text.strip(need_tobe_delete))

    return jd['result']['count']['total']

print getCommentCounts('http://news.sina.com.cn/o/2017-03-01/doc-ifyazwha3457343.shtml')
print getCommentCounts('http://news.sina.com.cn/c/nd/2017-03-01/doc-ifycaafm4652808.shtml')
print getCommentCounts('http://news.sina.com.cn/o/2017-03-01/doc-ifycaasy7203725.shtml')
print getCommentCounts('http://news.sina.com.cn/c/nd/2017-03-02/doc-ifycaafm4749387.shtml')