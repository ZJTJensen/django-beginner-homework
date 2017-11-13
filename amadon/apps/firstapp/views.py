# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, 'firstapp/index.html')

def process(request):
    
    request.session['subtotal'] = float(request.POST['price']) * float(request.POST['nums'])
    total = 0
    counter =0
    
    total = total + float(request.session['subtotal'])
    request.session['total'] = total
    
    counter = float(request.POST['nums']) + counter
    request.session['counter']= counter 
    return render(request, 'firstapp/checkout.html')




# Create your views here.
