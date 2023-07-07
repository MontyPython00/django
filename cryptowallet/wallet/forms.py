from django import forms
from wallet import models
from django.forms import ModelForm

class SignInForm(forms.Form):
	login = forms.EmailField(label='Email:', widget=forms.EmailInput(attrs={'class':'form-control'}))
	password = forms.CharField(label = 'Password:', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'})
)
class SearchEngineForm(forms.Form):
	search = forms.CharField(max_length=40, label='Coin:', widget=forms.TextInput(attrs={'class':'form-control'}))
	
class AccountForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = models.Account
		fields=['login', 'password']
		

