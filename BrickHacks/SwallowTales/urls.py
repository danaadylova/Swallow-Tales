__author__ = 'danaadylova'

from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
    url(r'^$', views.startPage, name='home'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^signup/', views.sign_up_view, name='signup'),
    url(r'^muh-stories/', views.stories, name='stories'),
    ]