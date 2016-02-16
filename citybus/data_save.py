# coding:utf-8
from citybus.models import LineTypes, CityList,CityBusStations,CityBusLines


class DataSave(object):
    def __init__(self):
        pass

    def savetypels(self, city=CityList(), parseres=''):
        if len(parseres) < 1:
            return 0
        for bustype in parseres:
            linetype = LineTypes.objects.get_or_create(
                    typename=bustype.get_text(),
                    fetchurl = city.cityurl + bustype['href'],
                    city=city)[0]
            print(linetype)
        return len(parseres)

    def savebusls(self,linetype=LineTypes(),buslines=''):
        if len(buslines)<1:
            return 0
        for xlh in buslines:
            busline=CityBusLines.objects.get_or_create(
                xlh=xlh.get_text(),
                fetchurl=linetype.city.cityurl+xlh['href'],
                city=linetype.city,
                linetype=linetype
            )[0]
            print busline
        return len(buslines)

    def savestations(self, busline, stations):
        upcnt=0
        downcnt=0
        try:
            for st in stations['up']:
                CityBusStations.objects.get_or_create(
                zdm=st.get_text(),
                updown=0,
                zdxh=upcnt,
                busline=busline
                )
                upcnt+=1
            for st in stations['down']:
                CityBusStations.objects.get_or_create(
                zdm=st.get_text(),
                updown=1,
                zdxh=downcnt,
                busline=busline
                )
                downcnt+=1
        except:
            return (upcnt,downcnt)
        return (upcnt,downcnt)


