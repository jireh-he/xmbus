# -*- coding: utf-8 -*-
from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import CityBusStations,CityBusLines,CityList
from busfunction import StationSearch
# Create your views here.
#默认从厦门开始
ONE_PAGE_OF_DATA=15
def stationsview(request):
    curPage=29
    cityid=370
    try:
        curPage=int(request.GET['curPage'])
        cityid=int(request.GET['cityid'])
        pageType=str(request.GET['pageType'])
        allPage=int(request.GET['allPage'])
    except:
        pageType=''
        allPage=1

    if pageType=='down':
        curPage+=1
    if pageType=='up':
        curPage-=1

    startPos=(curPage-1)*ONE_PAGE_OF_DATA
    endPos=startPos+ONE_PAGE_OF_DATA
    cities=CityList.objects.all()[startPos:endPos]
    if allPage==1:
        totalcnt=CityList.objects.count()
        allPage=totalcnt/ONE_PAGE_OF_DATA
        remaincnt=totalcnt%ONE_PAGE_OF_DATA
        if remaincnt>0:
            allPage+=1

    if curPage>allPage:
        curPage=allPage

    startPage=curPage-4
    endPage=curPage+6
    if startPage<1:
        startPage=1
        endPage=11
    if endPage>allPage:
        endPage=allPage+1
        startPage=allPage-10
    pageRange=range(startPage,endPage)
    zhandian=CityBusStations.objects.filter(busline__city_id=cityid,jingdu__isnull=True,weidu__isnull=True)[:40]
    stations=[]
    cityname=zhandian[0].busline.city.cityname
    for z in zhandian:
        ss=StationSearch(stations,z.zdm)
        xlh=ss.getxlhlist()
        if xlh is None:
            xlh=[z.busline.xlh]
        else:
            xlh.append(z.busline.xlh)
        xlh=list(set(xlh))
        stations=ss.updatezdm(xlh)
    return render(request, 'citybus/citybus.html',
                  {
                    "stations":stations,
                    "cities":cities,
                    "curPage":curPage,
                    "allPage":allPage,
                    "pageRange":pageRange,
                    "cityid":int(cityid),
                    "cityname":cityname,
                   }
                  )

#保存坐标
def savepoints(request):
    dict={}
    info='success'
    try:
        if request.method=='POST':
            jsondata=json.loads(request.POST['jsondata'])
            cityid=request.POST['cityid']
        dict['zdm']=[]
        dict['cityid']=cityid
        for row in jsondata:
            zdm=row[0].replace('(',u'︵' ).replace( ')',u'︶')

            if row[2].strip():
                jingdu=row[2]
                weidu=row[3]
                gpslng=row[4]
                gpslat=row[5]
                dict['zdm'].append(zdm)
                CityBusStations.objects.filter(zdm=zdm,
                                               busline__city_id=cityid).update(jingdu=jingdu,
                                                                               weidu=weidu,
                                                                               gpslng=gpslng,
                                                                               gpslat=gpslat)


    except:
        import sys
        info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])
    dict['message']=info
    return JsonResponse(dict)


