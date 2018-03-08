from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ['profile_pic']
