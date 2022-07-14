from django.urls import path
from news.views import NewsList, NewsCreate

urlpatterns = [
    path('', NewsList.as_view()),
    path('create/', NewsCreate.as_view())
]
