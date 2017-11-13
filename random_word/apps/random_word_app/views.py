# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def index(request):
    try:
            request.session['tries']
    except KeyError:
        request.session['tries'] = 0
    # return render(request,'random_word_app/index.html', context)
    return render(request,'random_word_app/index.html')

def generate(request):
    request.session['tries'] += 1
    request.session['random_number'] = get_random_string(length=12)
    return redirect('/')
def reset(request):
    del request.session['tries']
    return redirect('/')


# Create your views here.
