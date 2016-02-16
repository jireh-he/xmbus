# coding:utf-8
import os
import sys

sys.path.append(os.path.abspath(".."))
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xmbus.settings")
application = get_wsgi_application()
from citybus import html_parser, data_save, url_manager, html_downloader

reload(sys)
sys.setdefaultencoding("utf-8")


class SpiderMain(object):
    def __init__(self):
        self.urlmng = url_manager.UrlManger()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.datasave = data_save.DataSave()

    def craw(self):
        cityls = self.urlmng.getcityls()
        typels = self.urlmng.gettypels()
        buslines = self.urlmng.getbuslines()
        '''
        for city in cityls:
            if self.urlmng.hasbustype(city):
              #  print city.cityname, '已抓取'
                continue
            else:
                print '成功抓取%s%s条记录' % (city.cityname, self.crawtype(city))
        for linetype in typels:
            if self.urlmng.haslines(linetype):
                print linetype.typename, '已抓取'
                continue
            else:
                print '开始抓取', linetype.city.cityname, linetype.typename, linetype.fetchurl
                print '成功抓取%s%s%s条记录' % (linetype.city.cityname, linetype.typename, self.crawbus(linetype))
      '''
        for line in buslines:
            if self.urlmng.has_station(line):
                #print line.city, line, '已抓取'
                continue
            else:
                print '开始抓取', line.city, line.xlh
                res=self.crawstation(line)
                print '成功抓取', line.city, line.xlh, '的站点信息,上行:',res[0],'下行:',res[1]

    def crawtype(self, city):
        htmldoc = self.downloader.download(city.cityurl)
        # 解析公交车分类信息
        # <div class="bus_layer_r">
        parseres = self.parser.parsehtml(htmldoc, 'div', 'bus_layer_r')
        return self.datasave.savetypels(city, parseres)

    def crawbus(self, linetype):
        htmldoc = self.downloader.download(linetype.fetchurl)
        # 解析公交车线路号信息
        # <div class="bstie_list">
        parseres = self.parser.parsehtml(htmldoc, 'div', 'stie_list')
        return self.datasave.savebusls(linetype, parseres)

    def crawstation(self, busline):
        htmldoc = self.downloader.download(busline.fetchurl)
        # 解析公交车线路具体信息，运行时间，票价，公交公司
        # <div class="bus_i_content">
        lineinfo = self.parser.lineinfo(htmldoc, 'div', 'bus_i_content')
        busline.gjgs=lineinfo['gjgs']
        busline.pjxx=lineinfo['pjxx']
        busline.yxsj=lineinfo['yxsj']
        #解析上下行的方向
        #<span class="bus_line_txt">3路公交车线路(莲花五村—第一码头)
        fangxiang=self.parser.fangxiang(htmldoc,'span','bus_line_txt')
        try:
            busline.sxfx=fangxiang['sxfx']
            busline.xxfx=fangxiang['xxfx']
        except:
            pass
        busline.save()
        #解析上下行的站点
        #<div class="bus_line_site ">
        stations=self.parser.stations(htmldoc,'div','bus_line_site')
        return self.datasave.savestations(busline,stations)



if __name__ == "__main__":
    bus_spider = SpiderMain()
    bus_spider.craw()
