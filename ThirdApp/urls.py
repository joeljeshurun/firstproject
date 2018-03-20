from django.urls import path
from ThirdApp import views

app_name='ThirdApp'
urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special,name='special')
]