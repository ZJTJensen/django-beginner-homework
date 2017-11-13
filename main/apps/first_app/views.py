# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
def index(request):
    responce = "Hello there how do you do?"
    return HttpResponse(response)

# def index(request):
#     context = {
#         "email" : "blog@gmail.com",
#         "name" : "mike"
#     }
#     return render(request, "ourApp/index.html", context)

# Create your views here.
