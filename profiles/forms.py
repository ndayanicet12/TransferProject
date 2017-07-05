from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from profiles.models import User
#from transfers.models import *

class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)

    class Meta:
        model = User
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
	

    class Meta:
        model = User
        fields = ("email",)
 
