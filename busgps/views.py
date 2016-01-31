# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from .models import Bd_Buslines


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def getBuslines(request):
    return render(request, 'buslines.html', {})


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
