from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.first_name}'


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ManyToManyField(Author, related_name='author')
    isbn = models.CharField(max_length=100)
    release_year = models.IntegerField()
    pages_amount = models.IntegerField()
    