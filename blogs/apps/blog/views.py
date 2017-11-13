# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = request.POST['name']
        request.session['counter'] = 100 # more on session below
        print "*"*50
        return render(request, 'blog/index.html')
    else:
        return render(request, 'blog/index.html')
def index(request):
    return HttpResponse('placeholder to later display all the list of blogs')
def new(request):
    return HttpResponse("placeholder to display a new form o creaate a new blog")
def newcreate(request):
    return redirect('/blogs')
def show(request):
    return HttpResponse("placeholder to display blog number")
def edit(request):
    return HttpResponse('placeholder to edit blog nmber')
def destroy(request):
    return redirect('/blogs')

# Create your views here.
