# coding=utf-8
# 加上第一行才能中文注释

# import requests
# newsurl = 'http://news.sina.com.cn/china/'
#
# res = requests.get(newsurl)
#
# res.encoding = 'utf-8'
# print res.text

from bs4 import BeautifulSoup
############################
#导入modules，import与from...import的不同之处在于，简单说：
# 如果你想在程序中用argv代表modules.argv，
# 则可使用：from modules import argv
# 一般说来，应该避免使用from..import而使用import语句，
# 因为这样可以使你的程序更加易读，也可以避免名称的冲突
###########################

html_sample = '<div class="news-item  ">\
					<h2><a href="http://news.sina.com.cn/c/sd/2016-11-28/doc-ifxyawmm3624224.shtml" target="_blank">雾霾中现耐药菌人类将面临无药可医？揭秘真相</a></h2>\
							<div class="info clearfix ">\
								<div class="time">11月28日 11:35</div>\
								<div class="action"><a href="http://comment5.news.sina.com.cn/comment/skin/default.html?channel=gn&newsid=comos-fxyawmm3624224&style=0" target="_blank" data-id="gn:comos-fxyawmm3624224:0">评论</a><span class="spliter">|</span><span id="bdshare" class="bdshare_t bds_tools get-codes-bdshare" data="{text:"雾霾中现耐药菌人类将面临无药可医？揭秘真相",url:"http://news.sina.com.cn/c/sd/2016-11-28/doc-ifxyawmm3624224.shtml",pic:''}"><span class="bds_more">分享</span></span></div>\
							</div>'

# html_sample = '<div class="news-item logout-news-item " data-sudaclick="news_important_logiout_3" id="logoutNewsItem">\
# <div><span class="close" suda-uatrack="key=newschina_index_2014&amp;value=close"><a href="javascript:;" onclick="document.getElementById("logoutNewsItem").className="news-item logout-news-item logout-news-item-hide";">Close</a></span>\
# <script type="text/javascript">\
# 						(function(){\
# 							var list = [\
# 			"据说登录微博后看新闻，年终奖会变多，试试？",\
# 			"聚会插不上话？登陆微博看看朋友都在吐槽哪条新闻。",\
# 			"更多精彩内容登录可见",\
# 			"小伙伴们都在看什么新闻？登录微博你就知道！",\
# 			"想知道领导都在关注哪些新闻？登录微博尽在掌握！"\
# 							];\
# 							var index = Math.floor(Math.random() * 5);\
# 							document.write(list[index]);\
# 						})();\
# 						</script>\
# <span class="login" suda-uatrack="key=newschina_index_2014&amp;value=login"><a href="javascript:;" id="newsWeiboLogin">登录</a></span></div>\
# </div>'

soup = BeautifulSoup(html_sample,'html.parser')
print soup.text

# soup.select可以找出含有对应标签的元素，返回一个list
header_div = soup.select('div')# 含div标签
header_alink = soup.select('a') # 含a标签
header_h2 = soup.select('h2') # 含h2标签

print len(header_div) #header_div含有四个元素
print header_div[2]

print len(header_alink) #header_alink含有两个元素
print header_alink
print header_alink[0].text #输出第一个元素其中内容
for link in header_alink:# 输出所有元素的内容
    print link.text

# 取出某个属性值
print header_alink[0]['target'] # 取出header_alink第一个元素中的target属性内容
for link in header_alink:# 找出所有href属性的内容（网址）
    print link['href']

print len(header_h2) # header_h2只有一个元素
print header_h2

print '#############################'
# 使用select找出所有class为time的元素（time前面需加'.'）
for link in soup.select('.news-item'):
    print link

# 使用select找出所有id为bdshare的元素（bdshare前面需加'#'）
for id in soup.select('#bdshare'):
    print id

print soup.select('h2')

str1 = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fycaafm4652808&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
str2 = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=sh&newsid=comos-fycaafm4652808&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
print str2==str1
print len(str1),len(str2)