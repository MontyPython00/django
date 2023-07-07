from django.urls import path
from coins import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns=[
    path('market/<str:name>/', views.CoinDetailView.as_view()),
    path('market_list/', views.CoinListViewAPI.as_view()),
    path('', views.CoinListCreateViewAPI.as_view()),
    path('<int:pk>/', views.CoinDetailViewAPI.as_view()),
    path('<int:pk>/update/', views.CoinUpdateViewAPI.as_view()),
    path('<int:pk>/delete/', views.CoinDeleteViewAPI.as_view()),
    path('auth/', obtain_auth_token),
]