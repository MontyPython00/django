from django.shortcuts import render, redirect
from wallet import forms, models
from django.urls import reverse

# Create your views here.


    
def register(request):

    if request.method == 'POST':
        
        form = forms.AccountForm(request.POST)
        
        if form.is_valid():
            
            user_email = form.cleaned_data['login']
            id_account = models.Account.objects.filter(login__contains=user_email)

            if len(id_account) == 0:
                
                # form.save()
                context = {'form': form,
                           'valid_email':True}
                
            else:

                context = {'form': form,
                'invalid_email': True}
        else:

            context = {'form': form,
                'invalid_email': True}

            
    else:

        form = forms.AccountForm
        context = {'form': form}  

                  
    return render(request, 'wallet/register_form.html', context=context) 

def index(request):
    return render(request, 'wallet/test.html')
    

def home(request):
    
    if request.method == 'POST':
        form = forms.SignInForm(request.POST)
        if form.is_valid():

            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            id_account = models.Account.objects.filter(login__contains=login)

            if len(id_account)>0:
                valid_login = id_account.get().login
                valid_pass = id_account.get().password
                if (valid_login == login) and (valid_pass == password):
                    context = {'account': True,
                            'user':login,
                            'form':form}
                else:
                    context = {'account': False,
                    'form': form,
                    'invalid_data': True}
                
            else:
                context = {'account': False,
                'form': form,
                'invalid_data': True}
                
    else:
        form = forms.SignInForm
        context = {'account': False,
        'form': form}

    return render(request, 'wallet/home_page.html', context=context)	
    

def pricing(request):
    form = forms.SearchEngineForm
    if request.method == 'POST':
        form = forms.SearchEngineForm(request.POST)
        if form.is_valid():
            
            result = form.cleaned_data['search']
            context = {'coins':models.Pricing.objects.filter(name__startswith=result),
            'form':form}
            return render(request, 'wallet/pricing.html', context=context)
        
    else:
        form = forms.SearchEngineForm
        context= {'coins': models.Pricing.objects.all(),
                'form':form}
        return render(request, 'wallet/pricing.html', context=context)
