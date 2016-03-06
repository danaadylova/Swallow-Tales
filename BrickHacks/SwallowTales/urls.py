__author__ = 'danaadylova'

from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
    url(r'^$', views.startPage, name='homepage'),
    url(r'^login/$', views.loginPage),
    url(r'^logout/$', views.logoutPage),

    ]