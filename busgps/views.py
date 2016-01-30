# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from .models import Bd_Buslines

# Create your views here.
def index(request):
        return render(request,'index.html',{})

def getBuslines(request):
    return render(request,'buslines.html',{})

def saveBuslines(request):
    cnt=0
    bsdata=request.POST
    cnt=str(bsdata)
    for k,v in bsdata.iteritems():
        break
        Bd_Buslines.objects.get_or_create(xlh=bsdata[k][0],zdm=bsdata[k][1],jingdu=bsdata[k][2],weidu=bsdata[k][3])
        cnt=cnt+1
    
    return JsonResponse({'cnt':cnt,});
