from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.login),
    path('register',views.register),
    path('porders',views.porders, name='pOs'),
    path('vorders',views.vorders, name='vOs'),
    path('invoice',views.invoice, name='inv'),

]