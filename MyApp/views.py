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
        print(form.is_valid())
        form = FormName(request.POST)
        if form.is_valid():
            form.save()

            # first = form.cleaned_data['first_name']
            # last = form.cleaned_data['last_name']
            # email = form.cleaned_data['email_id']

            #User.objects.get_or_create(first_name=first, last_name=last, email_id=email)
            # user = User(first_name=first, last_name=last, email_id=email)
            # user.save()
    return render(request, 'MyApp/form_details.html',{'form':form})

