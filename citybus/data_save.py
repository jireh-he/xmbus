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

    def savestations_points(self,busline,stations):
        upcnt=0
        downcnt=0
        for st in stations['up']:
            point1=self.jiemi(st['p'])
            #print st['zdm'],point
            cbs=CityBusStations.objects.get_or_create(
            zdm=st['zdm'],
            updown=0,
            zdxh=upcnt,
            jingdu=point1[0],
            weidu=point1[1],
            busline=busline
            )
            upcnt+=1
        for st in stations['down']:
            point2=self.jiemi(st['p'])
            #print st['zdm'],point
            CityBusStations.objects.get_or_create(
            zdm=st['zdm'],
            updown=1,
            zdxh=downcnt,
            jingdu=point2[0],
            weidu=point2[1],
            busline=busline
            )
            downcnt+=1
        return (upcnt,downcnt)

    #解密百度坐标字符串
    def jiemi(self,a):
        if a is None or a=='':
            return [0,0]
        c,e,b=-1,0,""
        for d in range(0,len(a)):
            f=int(a[d],36)-10
            if f>=17:
                f-=7
            b+=self.ten36(f)
            if f>e:
                c=d
                e=f
        a=int(b[0:c],16)
        c=int(b[c+1:],16)
        b=[]
        b.append((a+c-3409)/2)
        b.append(c-b[0])
        b[0]/=1000000.0
        b[1]/=1000000.0
        return b

    #十进制转36进制
    def ten36(self,ten):
        if ten==0:
            return u"0"
        loop='0123456789abcdefghijklmnopqrstuvwxyz'
        a=[]
        while ten!=0:
            a.append(loop[ ten % 36])
            ten=ten/36
        a.reverse()
        out=''.join(a)
        return  out

