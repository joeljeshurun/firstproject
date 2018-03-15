from django.urls import path
from MyApp import views


app_name= 'MyApp'
urlpatterns =[
    path('index/',views.index,name='index'),
    path('users/',views.user, name='user'),
    path('formdetails/',views.form_detail_view, name='formdetails'),
    path('relative/', views.relative, name='relative'),
    path('home/',views.home, name='home')

]