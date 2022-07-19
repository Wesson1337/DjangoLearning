from django.urls import path
from goods import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('update_prices/', views.update_prices, name='update_prices')
]
