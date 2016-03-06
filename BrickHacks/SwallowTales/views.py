from django.http import *
from django.shortcuts import render_to_response,redirect, render
from django.template import RequestContext
from SwallowTales.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login, logout
from SwallowTales.forms import UserForm

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
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            new_user.save()
            # redirect, or however you want to get to the main view
            return redirect('SwallowTales.views.login_view')
        else:
            return redirect('SwallowTales.views.sign_up_view')
    else:
        form = UserForm()
    return render(request, 'sign_up.html', {'form': form})

def stories(request):
    return render(request, 'muh_storiez.html')
