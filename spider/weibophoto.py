#coding=utf-8
__author__ = 'wang'
import urllib2
import re

# class Weibo:
#     def __init__(self):
#         self.siteURL='http://weibo.com/3177527181/DloNmjU2R?type=comment#_rnd1457489286755'
#     def getPage(self):
#         url=self.siteURL
#         request=urllib2.Request(url)
#         response=urllib2.urlopen(request)
#         print response.read().decode('gbk')
#         return response.read().decode('gbk')
#
#
# weibo=Weibo()
# weibo.getPage()
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import urllib2
import json
import re
url = 'http://weibo.com/aj/v6/comment/big?ajwvr=6&id=3951002044743673&max_id=3951150182480453&page=2&__rnd=1457512456542'

l = urllib2.Request(url)
print l
ldata=urllib2.urlopen(l).read()
print ldata
# jdata = json.loads(ldata)
# print jdata

