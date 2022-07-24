from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    code = models.CharField(max_length=100, verbose_name='code')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')


class ItemNew(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')
    weight = models.FloatField(verbose_name='вес')

    def __str__(self):
        return f'{self.name}'
