from django import forms
from django.forms import TextInput

from .models import Porders


class ViewPlacedOrders(forms.ModelForm):
    class Meta:
        model = Porders
        fields = ['firstname', 'lastname' , 'phonenumber','orderquantity','country','zipcode','address','shipmentmode']
        labels = {'firstname':'First Name', 'lastname':'Last Name' , 'phonenumber':'Phone Number','orderquantity':'Quantity','country':'Country','zipcode':'ZipCode','address':'Address','shipmentmode':'Shipment Mode'}


