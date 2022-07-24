from django.urls import path
from django.views.decorators.cache import cache_page
from pages import views

urlpatterns = [
    path('', cache_page(30)(views.translation_example), name='translation')
]
