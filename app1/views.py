from traceback import format_exc
from django.shortcuts import render
from app1.forms import RajForm , RajForm2
from app1.models import Raj

# Create your views here.
def index(request):
    form = RajForm()
    if request.method == 'POST':
        form = RajForm(request.POST)
        if form.is_valid():
            form.save()
            form = RajForm()
    return render(request,'app1/index.html',{'form':form})

def home(request):
    form = RajForm2()
    if request.method == 'POST':
        form = RajForm2(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            place = form.cleaned_data['place']
            phonenumber = form.cleaned_data['phonenumber']
            course = form.cleaned_data['course']
            chandu = Raj(name=name,email=email,place=place,phonenumber=phonenumber,course=course)
            chandu.save()
        else:
            print('invalid data')
        form = RajForm2()
    return render(request,'app1/home.html',{'form':form})
