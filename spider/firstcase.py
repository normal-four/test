#coding=utf-8
__author__ = 'wang'
import urllib
import urllib2
import re
page= 2
#url='http://www.qiushibaike.com/8hr/page/'+str(page)+'/?s=4856294'
url='http://www.qiushibaike.com/'
user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0)'
headers={'User-Agent':user_agent}
try:
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    content=response.read().decode('utf-8')
    pattern=re.compile('<div.*?author clearfix">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    items=re.findall(pattern,content)
    for item in items:
        haveImg=re.search("img",item[3])
        if not haveImg:
            print item[0],item[1],item[2],item[3],item[4]

    #print response.read()
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason