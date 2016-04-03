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
        for city in cityls:
            htmldoc=self.downloader.download(city.cityurl)
            cid=self.parser.getcid(htmldoc)
            city.cid=cid
            city.save()
            print '成功更新',city.cityname,'cid为',cid

if __name__ == "__main__":
    bus_spider = SpiderMain()
    bus_spider.craw()
