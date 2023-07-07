from django.urls import path
from wallet import views

app_name = 'wallet'

urlpatterns = [
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('signin/', views.register, name='signin')
]
