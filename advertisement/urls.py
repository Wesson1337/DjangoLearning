from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_list, name='get_client_ip'),
    path('about/', views.About.as_view(), name='about')
]
