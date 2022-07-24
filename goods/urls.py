from django.urls import path
from goods import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('update_prices/', views.update_prices, name='update_prices'),
    path('items/', views.items_list, name='item_list'),
    path('items_new', views.ItemList.as_view(), name='item_list_new'),
    path('items_new2', views.ItemListNew.as_view(), name='item_list_new2')
]
