# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect, render
import datetime


def index(request):
    return render(request, 'session/index.html')

def process(request):
    print "hello"
    now = datetime.datetime.now().isoformat()
    if 'words' not in request.session:
        request.session['words'] = []
    if 'size' in request.POST:
        font_size = 2
    else:
        font_size = 1
    context ={
        'word': request.POST['word'],
        'color': request.POST['radio'],
        'size': font_size,
        'time': now
    }
    request.session['words'].append(context)
    request.session.modified = True
    print context
    return redirect('/')

def clear(request):
    request.session['words']= []
    return redirect('/')

# Create your views here.
