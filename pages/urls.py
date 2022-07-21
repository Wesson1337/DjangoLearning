from django.urls import path

from pages import views

urlpatterns = [
    path('', views.translation_example, name='translation')
]
