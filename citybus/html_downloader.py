# coding:utf-8
import urllib2
class HtmlDownloader(object):
    def download(self, cityurl):
        if cityurl is None:
            return None
        response=urllib2.urlopen(cityurl)
        if response.getcode()!=200:
            return None
        return response.read()
