__author__ = 'danaadylova'

from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
    url(r'^$', views.startPage, name='home'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^signup/', views.sign_up_view, name='signup'),
    url(r'^muh-stories/', views.stories, name='muh-stories'),
    url(r'^add-story/', views.add_story, name='add-story'),
    url(r'^edit_section/([0-9]+)/', views.edit_section, name='edit_section'),
    url(r'^view_section/([0-9]+)/', views.view_section, name='view_section'),
    url(r'^add_alternative_section/([0-9]+)/', views.add_alternative_section, name='add_alternative_section'),
    url(r'^add_next_section/([0-9]+)/', views.add_next_section, name='add_next_section'),
    ]