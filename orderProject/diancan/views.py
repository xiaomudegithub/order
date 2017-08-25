# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

import json

from models import *

# Create your views here.

def login(request):
    userName = request.POST.get('userName')
    return HttpResponse("login")

def register(request):
    companyCode = request.GET.get("companyCode")
    if companyCode:
        quereCompany = Company.objects.get(companyId= int(companyCode))
        if quereCompany:
            userName = request.GET.get("userName")
            print userName
            newUser = User()
            newUser.userName = userName
            newUser.companyName = quereCompany.companyName
            newUser.save()
            return HttpResponse("register Success")
    return HttpResponse("register")

def userOrderInfos(request):
    return HttpResponse("orderInfos")

def orderList(request):
    return HttpResponse("orderList")

def order(request):
    return render("home.html",'')

