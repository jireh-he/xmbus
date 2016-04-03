# coding:utf-8
import urllib2
import urllib
import cookielib
import json
import time
MAX_TYIES=10
class HtmlDownloader(object):
    def download(self, cityurl):
        if cityurl is None:
            return None
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.add_headers = [('User-agent', 'Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 6.1; WOW64; Trident/5.0)'),
                              ('Referer',cityurl)]
        for tries in range(MAX_TYIES):
            try:
                urllib2.install_opener(opener)
                response=urllib2.urlopen(cityurl)
                if response.getcode()!=200:
                    return None
                return response.read()
            except:
                if tries<(MAX_TYIES-1):
                    time.sleep(10)
                    continue
                else:
                    return None
        return None

    def jsonfetch(self,url,jsondata):
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.add_headers = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
        urllib2.install_opener(opener)
        #req = urllib2.Request(url, data=urllib.urlencode(jsondata))
        #req.add_header('Referer', 'http://www.baidu.com')
        requrl=url+'?'+urllib.urlencode(jsondata)
        rep = urllib2.urlopen(requrl)
        resjson=json.loads(rep.read())
        if resjson["status"] == 0:
            try:
                jsres = resjson["result"][0]
                if resjson["result"][0]:
                    return jsres
            except:
                return None
        return None
