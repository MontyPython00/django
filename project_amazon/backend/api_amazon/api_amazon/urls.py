"""
URL configuration for api_amazon project.

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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from api_amazon import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('photo/<int:pk>/', views.test_img),
    path('api/items/', views.ItemListCreateViewAPI.as_view()),
    path('api/items/<int:pk>/', views.ItemDetailViewAPI.as_view()),
    path('api/items/<int:pk>/update/', views.ItemUpdateViewAPI.as_view()),
    path('api/items/<int:pk>/delete/', views.ItemDeleteViewAPI.as_view()),
    path('api/photos/', views.PhotoListCreateViewAPI.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
