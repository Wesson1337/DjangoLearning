from django.urls import path

from books.views import BookList, AuthorList

urlpatterns = [
    path('author/', AuthorList.as_view(), name='author_list'),
    path('books/', BookList.as_view(), name='book_list')
]
