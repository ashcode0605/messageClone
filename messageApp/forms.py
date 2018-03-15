from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . models import UserProfileInfo,Message
from django.contrib.auth.models import User
from pagedown.widgets import PagedownWidget

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ['profile_pic']

class MessageForm(ModelForm):
    message_body = forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta:
        model = Message
        fields = ['sent_to','message_body']