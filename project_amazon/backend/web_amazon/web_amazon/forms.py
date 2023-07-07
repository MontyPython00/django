from django import forms

class ItemForm(forms.Form):
    name= forms.CharField(max_length=70, required=True, widget=forms.TextInput(attrs={'class':'form-input', 'placeholder':'Name'}))
    description= forms.CharField(max_length=1024, widget=forms.Textarea(attrs={'class':'form-input', 'placeholder':'Here describe product...'}))
    price= forms.DecimalField(max_digits=7, decimal_places=2, required=True,widget=forms.NumberInput(attrs={'class':'form-input', 'placeholder':'Price'}),)



    
