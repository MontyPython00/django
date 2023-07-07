from django.urls import path
from market import views

app_name='market'

urlpatterns=[
    path('', views.MarketView.as_view(), name='market_home'),
    path('coin_form/', views.MarketFormView.as_view(), name='coin_form'),
    path('coinrequest_form/', views.CoinRequestCreate.as_view(), name='coinrequest_form'),
    path('coinrequest_list/', views.CoinListToApprove.as_view(), name='coinrequest_list'),
    path('coinrequest_list/<int:pk>', views.CoinListToApproveDetail.as_view()),
    path('coinrequest_list/update/<int:pk>', views.CoinListToApproveUpdate.as_view()),
    path('registration/', views.SignUpView.as_view(), name='register')

]