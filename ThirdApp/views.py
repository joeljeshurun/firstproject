from django.shortcuts import render
from ThirdApp import forms
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ThirdApp.models import UserProfileInfo

# Create your views here.

def index(request):
    return render(request,'ThirdApp/index.html')

def home(request):
    return render(request,'ThirdApp/home.html')

def register(request):
    register=False
    if request.method == 'POST':
        user_form=forms.UserForm(request.POST)
        profile_form=forms.UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            register=True
    else:
        user_form=forms.UserForm()
        profile_form=forms.UserProfileForm()
    return render(request,'ThirdApp/register.html',{'user_form': user_form, 'profile_form':profile_form,'register':register})

def user_login(request):
    if request.method=='POST':
        login_form=forms.UserLoginForm(request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                request.session['username']=username
                return HttpResponseRedirect(reverse('ThirdApp:index'))
            else:
                return HttpResponse("Invalid Login Details!")
    else:
        login_form=forms.UserLoginForm()
    return render(request,'ThirdApp/login.html',{'form':login_form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('ThirdApp:index'))

@login_required
def special(request):
    if request.session['username']:
        user = User.objects.get(username=request.session['username'])
        user_profile = UserProfileInfo.objects.get(user=user)
    else:
        print("expired")

    return render(request,'ThirdApp/special.html',{'user':user,'user_profile':user_profile})

@login_required
def delete_user(request):
    if request.session['username']:
        user = User.objects.get(username=request.session['username']).delete()
        del request.session['username']
        user_logout(request)
        return HttpResponseRedirect(reverse('ThirdApp:index'))
    else:
        return HttpResponse("Please login!")

@login_required
def edit_user(request):
    name=User.objects.get(username=request.session['username'])
    user_info=UserProfileInfo.objects.get(user=name)
    if request.method == 'POST':
        user_form=forms.EditUserForm(request.POST,instance=name)
        profile_form=forms.EditUserProfileForm(request.POST,request.FILES,instance=user_info)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('ThirdApp:index'))
    else:
        user_form=forms.EditUserForm(instance=name)
        profile_form=forms.EditUserProfileForm(instance=user_info)
    return render(request,'ThirdApp/edit.html',context={'user_form':user_form,'profile_form':profile_form})
