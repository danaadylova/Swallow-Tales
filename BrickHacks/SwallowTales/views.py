from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def startPage(request):
    return HttpResponse("Hello, this is the start page.")

def loginPage(request):
    return render(request, 'static/login.html')

def logoutPage(request):
    return HttpResponse("Hello, this is the logout page.")