# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 11:15:16 2017

@author: welcome
"""


import re
import urllib

# get jpg

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html
    
html= getHtml("https://tieba.baidu.com/p/2667879540")

def getImg(html):
    reg=r'src="(.*?\.jpg)"'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    return imglist
    
pic=getImg(html)

x=0
for imgurl in pic:
    urllib.urlretrieve(imgurl,'%s.jpg' % x)
    x+=1

