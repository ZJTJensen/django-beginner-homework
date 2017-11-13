# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse, redirect
import datetime
import random
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'messages' not in request.session:
        request.session['messages'] =''

    context={
        'messages': str(request.session['messages'])
    }
    return render(request, "ninjagold/index.html", context)

def process(request):
    now = datetime.datetime.now().isoformat()
    #if the farm button is pressed
    if request.POST['building'] == 'farm':
        earning=random.randrange(10, 21)
        request.session['gold'] += earning
        request.session['messages'] += "You made {} Gold {}".format(earning, now)
        return redirect('/')

    #give 10 -20 gold

    #if the cave button is pressed 
    elif request.POST['building'] == 'cave':
        earning=random.randrange(5, 11)
        request.session['gold'] += earning
        request.session['messages'] += "You made {} Gold {}".format(earning, now)
        return redirect('/')

    #give 5-10 gold

    #if house is pressed
    elif request.POST['building'] == 'house':
        print "Hello world"
        request.session['messages'] += "You sat at home and watched netflix all day {}".format(now)
        return redirect('/')

    #output that they watched netflix

    #if the cassino is pressed
    elif request.POST['building'] == 'cassino':
        chance = random.randrange (0,2)
        if chance == 0:
            earning=random.randrange(0, 51)
            request.session['gold'] += earning

            request.session['messages'] += "You made {} Gold {}".format(earning, now)
        elif chance == 1:
            earning=random.randrange(0, 51)
            request.session['gold'] -= earning

            request.session['messages'] += "You Lost {} Gold {}".format(earning, now)
        return redirect('/')
    #risk 0 to 50 gold
# Create your views here.

def clear(request):
    request.session['messages']=''
    return redirect('/')
