# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from .models import Bd_Buslines
from django.db import connection

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def getBuslines(request):
    return render(request, 'busgps/buslines.html', {})


def saveBuslines(request):
    bsdata = request.POST.lists()
    forloop=0
    for k, v in bsdata:
        if len(v) == 5:
            forloop+=1
            flag=Bd_Buslines.objects.get_or_create(xlh=v[0], zdm=v[1], jingdu=v[2], weidu=v[3], zdxh=v[4],updown='1')
            if not flag:
                print v
    return JsonResponse({'cnt': forloop})

def countperday(request):
    cursor=connection.cursor()
    sql=r"select * from  MV_BUSGPS_OLDMAN_STATICS"
    raw=cursor.execute(sql)
    statics=raw.fetchall()
    skrc=[]
    cxrs=[]
    lrskcs=[]
    lrcxrs=[]
    for st in statics:
        skrc.append({"riqi":st[0],"num":st[1]})
        cxrs.append({"riqi":st[0],"num":st[2]})
        lrskcs.append({"riqi":st[0],"num":st[3]})
        lrcxrs.append({"riqi":st[0],"num":st[4]})
    return JsonResponse({"dataset":[
        {"name":"刷卡人次","cnt":skrc},
        {"name":"出行人数","cnt":cxrs},
        {"name":"老人刷卡次数","cnt":lrskcs},
        {"name":"老人出行人数","cnt":lrcxrs},
    ]})

def oldmanheat(request):
    cursor=connection.cursor()
    sql=r"""select t.jingdu,t.weidu,round(avg(t.oldman)) as count from MV_OLDMAN_RIQI_FENBU t
where t.jingdu>0
group by t.jingdu,t.weidu
order by  avg(t.oldman) desc"""
    raw=cursor.execute(sql)
    heats=raw.fetchall()
    points=[]
    for h in heats:
        points.append({"lng":float(h[0]),"lat":float(h[1]),"count":int(h[2])})
    return JsonResponse({
        "heatarr":points
    })

def theolds(request):
    return render(request,'busgps/theolds.html',{})