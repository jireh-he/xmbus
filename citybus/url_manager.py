# coding:utf-8
from citybus.models import LineTypes,CityList,CityBusStations,CityBusLines
class UrlManger(object):
    def __init__(self):
        pass
    def getcityls(self):
        return CityList.objects.all()
    def gettypels(self):
        return LineTypes.objects.all()
    def getbuslines(self):
        return CityBusLines.objects.all()

    def getstations(self,cityid):
        return CityBusStations.objects.filter(busline__city_id=cityid);

    def hasbustype(self,city):
       return LineTypes.objects.filter(city=city)

    def haslines(self,linetype):
        return CityBusLines.objects.filter(linetype=linetype)

    def has_station(self,line):
        return CityBusStations.objects.filter(busline=line)


