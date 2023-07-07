from typing import Any, Dict, Optional, Type
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.views import generic
from market import forms
import requests
from market.models import CoinRequest
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class SignUpView(generic.CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='registration/register.html'


class MarketView(generic.TemplateView):
    template_name='market/home.html'
    
    
    def get_context_data(self, **kwargs):

        if self.request.GET.get('coin') is None:
            endpoint='http://localhost:8000/api/coins/market_list'

            response= requests.get(endpoint)
            req=response.json()
            
            
            context={'coins':req,
                     'list':True}
            
            return context
        
        else:
            coin=self.request.GET.get('coin')
            endpoint=f'http://localhost:8000/api/coins/market/{coin}/'
            response=requests.get(endpoint)
            req=response.json()

            context={'detail':req,
                     'list':False}
            return context
    
    



class MarketFormView(LoginRequiredMixin, generic.FormView):
    form_class=forms.CoinRequestForm
    template_name= 'market/coin_request_API.html'

    success_url='/market/'

    def form_valid(self, form):

        endpoint='http://localhost:8000/api/coins/auth/'
        user=form.cleaned_data['login']
        password=form.cleaned_data['password']
        data={
            'username':user,
            'password':password
        }

        auth_response= requests.post(endpoint, data=data)


        if auth_response.status_code==200:
            token= auth_response.json()['token']
            name=form.cleaned_data['name']
            description=form.cleaned_data['description']
            price=form.cleaned_data['price']
            headers={
                    'Authorization': f'Token {token}'
            }
            endpoint='http://localhost:8000/api/coins/'

            data={
                    'name':name,
                    'description':description,
                    'price':price
                    }

            requests.post(endpoint, headers=headers, json=data)
        
            
        
        return super().form_valid(form)
    


class CoinRequestCreate(LoginRequiredMixin, generic.CreateView):
    model=CoinRequest
    fields=['name', 'description', 'price']
    success_url=reverse_lazy('market:coinrequest_list')
    


class CoinListToApprove(LoginRequiredMixin, generic.ListView):
    template_name='coinrequest_list.html'
    model=CoinRequest



class CoinListToApproveDetail(LoginRequiredMixin, generic.DetailView):
    model= CoinRequest



class CoinListToApproveUpdate(LoginRequiredMixin, generic.UpdateView):
    model=CoinRequest
    fields=['status']
    success_url=reverse_lazy('market:coinrequest_list')
    template_name_suffix='_update'

    

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        coin=super().get_context_data()['object']
        status=form.cleaned_data['status']
        
        if status == 'a':
            endpoint='http://localhost:8000/api/coins/auth/'
            data={
                'username':'admin',
                'password':'admin',
            }

            auth_response= requests.post(endpoint, data=data)


            if auth_response.status_code==200:
                token= auth_response.json()['token']
                name=coin.name
                description=coin.description
                price=coin.price
                headers={
                        'Authorization': f'Token {token}'
                }
                endpoint='http://localhost:8000/api/coins/'

                data={
                        'name':name,
                        'description':description,
                        'price':price
                        }

                requests.post(endpoint, headers=headers, json=data)
                CoinRequest.objects.get(pk=coin.id).delete()
                return HttpResponseRedirect(reverse('market:coinrequest_list'))
                
        elif status == 'd':
            CoinRequest.objects.get(pk=coin.id).delete()
            return HttpResponseRedirect(reverse('market:coinrequest_list'))
        return super().form_valid(form)
    
    