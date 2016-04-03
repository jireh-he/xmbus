# coding:utf-8
import os
import sys
import re
import datetime
sys.path.append(os.path.abspath(".."))
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xmbus.settings")
application = get_wsgi_application()
from citybus import html_parser, data_save, url_manager, html_downloader

reload(sys)
sys.setdefaultencoding("utf-8")


class SpiderPoints(object):
    def __init__(self):
        self.urlmng = url_manager.UrlManger()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.datasave = data_save.DataSave()

    def craw(self):
        buslines = self.urlmng.getbuslines()
        for line in buslines:
            if self.urlmng.has_station(line):
                print line.city, line, '已抓取'
                continue
            print '开始抓取', line.city, line.xlh
            res=self.crawpoints(line)
            print '成功抓取', line.city, line.xlh, '的站点信息,上行:',res[0],'下行:',res[1]


    def crawpoints(self, busline):
        #解析上下行的站点的坐标
        #网站的坐标js是动态加载的，无法从源代码抓到，只能根据规则动态生成
        cid=busline.city.cid
        #<script type="text/javascript" src="http://shanghai.8684.cn/map/2_e7f50f37.js?1456207757" charset="UTF-8"></script>
        bsurl=re.match(r'http://(.+)/x_(.+)',busline.fetchurl)
        urlgroups=bsurl.groups()
        jsurl='http://'+urlgroups[0]+'/map/'+str(cid)+'_'+urlgroups[1]+'.js?'+str(datetime.datetime.now().microsecond)
        print jsurl
        jsdoc=self.downloader.download(jsurl)
        stations=self.parser.getstations(jsdoc)
        return self.datasave.savestations_points(busline,stations)




if __name__ == "__main__":
    bus_spider = SpiderPoints()
    bus_spider.craw()
