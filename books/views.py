from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from books.filters import BookFilter
from books.models import Author, Book
from books.serializers import BookSerializer, AuthorSerializer


class AuthorList(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name']


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
