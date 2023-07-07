from django import forms
from market.models import CoinRequest

class CoinRequestForm(forms.Form):
    login= forms.CharField(max_length=30, widget=forms.PasswordInput)
    password= forms.CharField(max_length=30, widget=forms.PasswordInput)
    name= forms.CharField(max_length=30)
    description=forms.CharField(widget=forms.Textarea)
    price=forms.IntegerField()


class CoinFormTest(forms.ModelForm):
    class Meta:
        model=CoinRequest
        fields=['name', 'description', 'price']
