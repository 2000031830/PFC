from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ViewPlacedOrders
from .models import Porders
def home(request):
    return render(request,'sdpApp2/home.html', {'title':'PFC-Home'})

def login(request):
    return render(request, 'sdpApp2/login.html')

def register(request):
    return render(request, 'sdpApp2/register.html')

def porders(request):
    if request.method=="POST":
        form = ViewPlacedOrders(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vOs')
    else:
        form = ViewPlacedOrders()
    return render(request, 'sdpApp2/porders.html',{'form':form})


def vorders(request):
    return render(request, 'sdpApp2/vorders.html',{'porders': Porders.objects.all()})

def invoice(request):
    return render(request,'sdpApp2/invoice.html',{'porders': Porders.objects.all()})