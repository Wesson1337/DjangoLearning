import django_filters
from books.models import Book


class BookFilter(django_filters.FilterSet):
    min_pages = django_filters.NumberFilter(field_name='pages_amount', lookup_expr='gte')
    max_pages = django_filters.NumberFilter(field_name='pages_amount', lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['author__first_name', 'author__last_name', 'name', 'pages_amount']
