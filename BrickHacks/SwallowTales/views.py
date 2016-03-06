from django.http import *
from django.shortcuts import render_to_response,redirect, render
from django.template import RequestContext
from SwallowTales.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login, logout
from django.contrib.auth.models import *
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
    if not request.user.is_authenticated():
        return redirect('home')
    my_stories_list = Story.objects.filter(author = request.user)
    return render(request, 'muh_storiez.html', {'my_stories_list': my_stories_list})


def add_story(request):
    if not request.user.is_authenticated():
        return redirect('home')
    if request.method == "POST":
        storyName = request.POST.get('name')
        sectionName = request.POST.get('secName')
        sectionText = request.POST.get('text')

        st = Story(author = request.user, name = storyName)
        st.save()
        section = StorySection(previousSection = None, author = request.user, story = st,
                               secName =sectionName ,
                               text = sectionText)
        section.save()
        return redirect('muh-stories')
    return render(request, 'add_story.html')