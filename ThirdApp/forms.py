from Tools.scripts.make_ctype import method
from django import forms
from ThirdApp.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields=['portfolio_site','profile_pic']


class UserLoginForm(forms.Form):

    username = forms.CharField(max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput())

class EditUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']

class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields=['portfolio_site','profile_pic']