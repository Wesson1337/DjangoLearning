from decimal import Decimal
from random import randint
from django.test import TestCase
from django.urls import reverse
from goods.models import Item

NUMBER_OF_ITEMS = 10


class ItemsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for item_index in range(NUMBER_OF_ITEMS):
            Item.objects.create(
                code=f'code {item_index}',
                price=Decimal(randint(1, 100))
            )

    def test_items_exists_at_desired_location(self):
        response = self.client.get('/goods/items')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goods/items_list.html')

    def test_items_number(self):
        response = self.client.get(reverse('items_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['items_list'] == NUMBER_OF_ITEMS)
