from django.urls import path
from MyApp import views

urlpatterns =[
    path('index/',views.index,name='index'),
    path('users/',views.user, name='user'),
    path('formdetails',views.form_detail_view, name='formdetails')

]