from django.shortcuts import render, redirect
from django.contrib.auth import decorators
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

import requests
import json

from web_amazon import forms

@decorators.login_required
def send_item_to_api(request):

    ItemForm= forms.ItemForm
    if request.method == 'POST':
        form=ItemForm(request.POST)
        if form.is_valid():
            endpoint= 'http://localhost:7000/api/items/'
            data= {
                'product':form.cleaned_data['name'],
                'item_owner':request.user.username,
                'price':json.dumps(form.cleaned_data['price'], default=int),
                'description': form.cleaned_data['description'],  
            }
    
            send_data= requests.post(endpoint, json=data)

    context={
        'item_form':ItemForm
    }

    return render(request, 'templates/web_amazon/item_form.html', context=context)



def retrieve_item_from_api(request):
    pk= request.GET.get('pk')

    if pk is not None:
        endpoint=f'http://localhost:7000/api/items/{pk}'
        retrieve_data=requests.get(endpoint)
        context={'data':retrieve_data.json(),
                 'pk':True}
        
        return render(request, 'templates/web_amazon/item_list.html', context=context)
    
    endpoint= 'http://localhost:7000/api/items/'
    retrieve_data= requests.get(endpoint)
    context= {'data':retrieve_data.json()}
    
    return render(request, 'templates/web_amazon/item_list.html', context=context)


@decorators.login_required
def user_profile(request):
    
    user= request.user.username
    endpoint= 'http://localhost:7000/api/items/'
    retrieve_items= requests.get(endpoint)
    pk= request.GET.get('pk')
    if request.method == 'POST':
        action= request.POST.get('action')
        if action == 'delete':
            endpoint= f'http://localhost:7000/api/items/{pk}/delete/'
            delete_item= requests.delete(endpoint)
            if delete_item.status_code == 204:
                print('Item removed')
            return redirect(reverse('profile'))

        if action == 'update':
            endpoint= f'http://localhost:7000/api/items/{pk}/update/'
            update_data= {'product': request.POST.get('title'),
                          'description': request.POST.get('description'),
                          'price': request.POST.get('price'),
                          'item_owner': request.user.username}
            send_update_item= requests.put(endpoint, json=update_data)
            send_update_item.json()
            return redirect(reverse('profile'))

    if retrieve_items.status_code == 200:
        items= retrieve_items.json()
        items_owner=[]
        for item in items:
            if user == item['item_owner']:
                items_owner.append(item)

        
        context={'items_owner':items_owner}
         
        
        
        if pk is not None:
            endpoint=f'http://localhost:7000/api/items/{pk}'
            retrieve_data=requests.get(endpoint)
            context={'items_owner':retrieve_data.json(),
                    'item_manager':True}

            return render(request, 'templates/web_amazon/profile.html', context=context)


            
    return render(request, 'templates/web_amazon/profile.html', context=context)




class UserCreateForm(generic.CreateView):
    form_class= UserCreationForm
    success_url=reverse_lazy('login')
    template_name= 'templates/registration/register.html'
