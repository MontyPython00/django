"""
URL configuration for web_amazon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from web_amazon import views

# app_name='web_amazon'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('items/create/', views.send_item_to_api, name='item_form'),
    path('items/', views.retrieve_item_from_api, name='item_list'),
    path('profile/', views.user_profile, name='profile'),
    path('register/', views.UserCreateForm.as_view(), name='register')
    # path('register/', views.create_account, name='register')
]
