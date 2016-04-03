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

BD_AK='BFcd9e84753ab8dcef34748bc43f952d'
BD_SUGGESTION_URL='http://api.map.baidu.com/place/v2/suggestion'
BD_GEOCONV_URL='http://api.map.baidu.com/geoconv/v1/'
class SpiderStations(object):
    def __init__(self):
        self.urlmng = url_manager.UrlManger()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.datasave = data_save.DataSave()

    def craw(self):
        cityls = self.urlmng.getcityls()
        for city in cityls:
            self.crawstations(city)

    def crawstations(self,city):
        station=self.urlmng.getstations(city.id).filter(jingdu__isnull=True,weidu__isnull=True)[0:1]
        if station is None or station.count()<1:
            return None
        station=station[0]
        zdm=city.cityname+station.zdm.replace(u'︵', '(').replace(u'︶', ')')
        jsondata={
            'query':zdm,
            'region':city.cityname,
            'output':'json',
            'ak':BD_AK,
            }
        bdres=self.downloader.jsonfetch(BD_SUGGESTION_URL,jsondata)
        if bdres is None or not bdres.has_key('location'):
            station.jingdu=station.weidu=station.gpslat=station.gpslng=0
            self.urlmng.getstations(city.id).filter(zdm=station.zdm).update(
            jingdu=station.jingdu,
            weidu=station.weidu,
            gpslng=station.gpslng,
            gpslat=station.gpslat
            )
            print zdm,'无法获取地址，暂时将坐标置为0，跳过'
            self.crawstations(city)
        station.jingdu=bdres['location']['lng']
        station.weidu=bdres['location']['lat']
        coords=str(bdres['location']['lng'])+','+str(bdres['location']['lat'])
        convdata={
            'coords':coords,
            'ak':BD_AK
        }
        gps=self.downloader.jsonfetch(BD_GEOCONV_URL,convdata)
        station.gpslng=2*station.jingdu-gps['x']
        station.gpslat=2*station.weidu-gps['y']
        self.urlmng.getstations(city.id).filter(zdm=station.zdm).update(
            jingdu=station.jingdu,
            weidu=station.weidu,
            gpslng=station.gpslng,
            gpslat=station.gpslat
        )
        print r'成功获取'+zdm+'的坐标，百度(',station.weidu,',',station.jingdu,'),GPS(',station.gpslat,',',station.gpslng,')'
        self.crawstations(city)
if __name__ == "__main__":
    station_spider = SpiderStations()
    station_spider.craw()
