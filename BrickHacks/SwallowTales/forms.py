__author__ = 'danaadylova'
from django.contrib.auth.models import User
from django.forms import ModelForm
from main.models import *


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'passwordConf')