__author__ = 'danaadylova'

from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
    url(r'^$', views.startPage, name='home'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
<<<<<<< Updated upstream
#    url(r'^sign_up/', views.sign_up_view, name='sign_up'),
=======
    url(r'^signup/', views.signup_view, name='signup'),
>>>>>>> Stashed changes
    ]