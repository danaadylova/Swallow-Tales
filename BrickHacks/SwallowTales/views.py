from django.http import *
from django.shortcuts import render_to_response,redirect, render
from django.template import RequestContext
from SwallowTales.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
# from SwallowTales.forms import StoryForm


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
    return redirect('home')

def sign_up_view(request):
    if request.user.is_authenticated():
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_conf = request.POST.get('password_conf')
        if password != password_conf:
            return redirect('signup')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = True
        user.save()
        var = authenticate(username=username, password=password)
        return redirect('home')
    return render(request, 'sign_up.html')

def stories(request):
    # if request.user.is_authenticated():
    #     return redirect('muh-stories')
    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     text = request.POST.get('text')
    #
    #     story = User.objects.create_user(username=username, email=email, password=password)
    #     return redirect('muh-stories')
    return render(request, 'muh_storiez.html')


def add_story(request):
    return render(request, 'add_story.html')