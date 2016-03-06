__author__ = 'danaadylova'
from django.contrib.auth.models import User
from django.forms import ModelForm
from SwallowTales.models import *


class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ('name', 'text')