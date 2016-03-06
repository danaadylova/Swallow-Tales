from django.http import *
from django.shortcuts import render_to_response,redirect, render
from django.template import RequestContext
from SwallowTales.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login, logout

# Create your views here.

def startPage(request):
    return render(request, 'home.html')

def login_view(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home.html')
    return render_to_response('login.html', context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return render(request, 'home.html')

def sign_up_view(request):
    return render(request, 'sign_up.html')