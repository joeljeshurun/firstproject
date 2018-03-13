from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    a=5+5
    my_dict={'insert_me':'inserted from view','second_key':'Again from view'}
    return render(request,'FirstApp/index.html',my_dict)

def home(request):
    return HttpResponse("WELCOME TO HOME")

def img(request):
    return render(request,'FirstApp/static_image.html')