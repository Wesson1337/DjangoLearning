from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    code = models.CharField(max_length=100, verbose_name='code')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')
