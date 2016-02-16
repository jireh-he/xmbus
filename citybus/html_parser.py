# coding:utf-8
from bs4 import BeautifulSoup
import re
class HtmlParser(object):
    def parsehtml(self, htmldoc, container, classname):
        soup=BeautifulSoup(htmldoc,'html.parser',from_encoding='utf-8')
        return soup.find(container,classname).find_all('a')

    def lineinfo(self, htmldoc, container, classname):
        soup=BeautifulSoup(htmldoc,'html.parser',from_encoding='utf-8')
        content=soup.find(container,classname).find_all('p','bus_i_t4')

        #运行时间:
        #<p class="bus_i_t4">运行时间：莲花五村 05:50-23:00|第一码头 05:40-23:15</p>
        yxsj=content[0].get_text().replace(r'运行时间：','')
        #票价信息
        #<p class="bus_i_t4">票价信息：全程一票制１元，E通卡８折</p>
        pjxx=content[1].get_text().replace(r'票价信息：','')
        #<p class="bus_i_t4">公交公司：厦门公交集团思明公司</p>
        gjgs=content[2].get_text().replace(r'公交公司：','')
        return {'yxsj':yxsj,'pjxx':pjxx,'gjgs':gjgs}

    def fangxiang(self, htmldoc,container, classname):
        soup=BeautifulSoup(htmldoc,'html.parser',from_encoding='utf-8')
        content=soup.find_all(container,classname)
        if 2 == len(content):
            return {'sxfx':content[0].get_text(),'xxfx':content[1].get_text()}
        elif len(content)==1:
            return {'sxfx':content[0].get_text()}
        else:
            return None

    def stations(self, htmldoc, container, classname):
        soup=BeautifulSoup(htmldoc,'html.parser',from_encoding='utf-8')
        content=soup.find_all(container,classname)
        if 2 == len(content):
            return {'up':content[0].find_all('a'),'down':content[1].find_all('a')}
        elif 1==len(content):
            return {'up':content[0].find_all('a')}
        else:
            return None

