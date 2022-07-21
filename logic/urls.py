from django.urls import path
from logic import views


urlpatterns = [
    path('', views.welcome, name='welcome')
]