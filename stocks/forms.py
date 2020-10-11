from django import forms
from .models import Userstock

class StockForm(forms.ModelForm):
    class Meta:
        model = Userstock
        fields = ["stockname","quantity","username","lastprice","action","cashvalue"]
