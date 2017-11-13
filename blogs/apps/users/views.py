
from django.shortcuts import render, HttpResponse, redirect
def regiter(request):
    return HttpResponse("Placeholder for users to create a new user record")
def login(request):
    return HttpResponse("placeholder for userrs to login")
def new(request):
    return redirect("/register")
def users(request):
    return HttpResponse("placeholder to latter display all the list of users")

# Create your views here.
