# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, 'surveys/index.html')

def process(request):
    request.session['namer'] = request.POST['namer']
    request.session['locations'] = request.POST['locations']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']
    return render(request, 'surveys/redirect.html')

# Create your views here.
