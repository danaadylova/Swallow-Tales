__author__ = 'danaadylova'
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')