from django.shortcuts import render
from MyApp.models import User
from MyApp.forms import FormName
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'MyApp/index.html')

def user(request):
    userlist = User.objects.order_by('first_name')
    mydict = {'user_list':userlist}
    return render(request,'MyApp/ShowUsers.html',context=mydict)

def form_detail_view(request):
    form = FormName()
    if request.method == 'POST':
        form = FormName(request.POST)
        if form.is_valid():
            print(form.cleaned_data['first_name'])
            print(form.cleaned_data['last_name'])
            print(form.cleaned_data['email_id'])
    return render(request, 'MyApp/form_details.html',{'form':form})

