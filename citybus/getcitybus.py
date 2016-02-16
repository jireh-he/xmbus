#!/usr/bin/env python
import os
import urllib
import urllib2
import cookielib
import sys
from bs4 import BeautifulSoup
import re
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xmbus.settings")
sys.path.append(os.path.abspath(".."))
from citybus.models import CityList,CityBuslines

def getcitylist():
    url='http://m.8684.cn/bus_switch'
    html_doc=fetchurl(url)
    soup=BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
    cityanchors=soup.find('section',class_='letterCon').find_all('a',href=re.compile(r'/*bus'))
    cityls=[]
    for ca in cityanchors:
        cityls.append((ca.get_text(),ca['href']))
    return cityls

def fetchurl(url,data={}):
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
    urllib2.install_opener(opener)
    if len(data)>0:
        req = urllib2.Request(url, data=urllib.urlencode(data))
    else:
        req = urllib2.Request(url)
    req.add_header('Referer', 'http://www.baidu.com')
    rep = urllib2.urlopen(req)
    return rep.read()

def savecitylist(cityls):
    savels=[]
    for cl in cityls:
        savels.append(CityList(cityname=cl[0],cityurl=r'http://m.8684.cn'+cl[1]))
    return CityList.objects.bulk_create(savels)

def main():
    """

    :rtype: object
    """
    cityls=getcitylist()
    print savecitylist(cityls)
    return


if __name__ == "__main__":
    main()
