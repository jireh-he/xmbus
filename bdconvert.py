#!/usr/bin/env python
import os
import urllib
import urllib2
import cookielib
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xmbus.settings")
from busgps.models import Bd_Buslines

def getbuspos():

    return list(set(Bd_Buslines.objects.filter(gpslat__isnull=True).values_list('jingdu', 'weidu')))


def convertpos(gpslist=[(0, 0)]):
    url = 'http://api.map.baidu.com/geoconv/v1/'
    ak = 'BFcd9e84753ab8dcef34748bc43f952d'
    if len(gpslist) >= 100:
        gpslist = gpslist[:99]
    result = []
    glist = []
    for g in gpslist:
        glist.append(str(g[0]) + ',' + str(g[1]))
        result.append({"jingdu": g[0], "weidu": g[1]})
    coords = ';'.join(glist)
    jsondata = {
        "coords": coords,
        "ak": ak,
    }
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
    urllib2.install_opener(opener)
    req = urllib2.Request(url, data=urllib.urlencode(jsondata))
    req.add_header('Referer', 'http://www.baidu.com')
    rep = urllib2.urlopen(req)
    resjson = json.loads(rep.read())
    if resjson["status"] == 0:
        jsres = resjson["result"]
        i = 0
        for gps in result:
            x = 2 * float(gps["jingdu"]) - jsres[i]['x']
            y = 2 * float(gps["weidu"]) - jsres[i]['y']
            result[i]["gpslng"] = x
            result[i]["gpslat"] = y
            i += 1
            print gps["jingdu"],',',gps["weidu"],'|',x,',',y
        return result
    else:
        return False

def updatepos(gpslist):
    cnt=0
    for gps in gpslist:
        cnt+=Bd_Buslines.objects.filter(jingdu=gps["jingdu"],weidu=gps["weidu"]).update(gpslng=gps["gpslng"],gpslat=gps["gpslat"])

    return cnt


def main():
    """

    :rtype: object
    """
    gplist = getbuspos()
    lslen=len(gplist)
    num=50
    if num>lslen:
        updatepos(convertpos(gplist))
    while num<=lslen:
        updatepos(convertpos(gplist[num-50:num]))
        num+=50
        if num>lslen:
            num=lslen
    return


if __name__ == "__main__":
    main()
