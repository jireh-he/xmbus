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

    #获取js地址
    def getcid(self,htmldoc):
        soup=BeautifulSoup(htmldoc,'html.parser',from_encoding='utf-8')
        jsurl=soup.find('script',attrs={"type":r'text/javascript',"src":re.compile(r'http://.+/(\d+).js$')})['src']
        res=re.split('\.|/',jsurl)
        cid=res[5]
        return  cid

    #解析获取的js脚本，获取所有公交站列表
    def getstations(self,jsdoc):
        pat=re.compile(r'Array\(.+\)')
        arrs=pat.findall(jsdoc)
        pat1=re.compile(r'".*?"')
        line={"up":[],"down":[]}
        if arrs and arrs[0]:
            line['up']=pat1.findall(arrs[0])
            if len(arrs)>1:
                line['down']=pat1.findall(arrs[1])
        upstations=[]
        cnt=0
        for up in line['up']:
            if cnt < 7:
                cnt += 1
                continue
            station=re.split(r'\|',up)
            point=None
            zdm=''
            if station and len(station)>2:
                point=station[0][1:]
                zdm=station[1]
            upstations.append({"p":point,"zdm":zdm})

        downstations=[]
        cnt=0
        for down in line['down']:
            if cnt < 7:
                cnt += 1
                continue
            station=re.split(r'\|',down)
            point=None
            zdm=''
            if station and len(station)>2:
                point=station[0][1:]
                zdm=station[1]
            downstations.append({"p":point,"zdm":zdm})
        return {"up":upstations,"down":downstations}


