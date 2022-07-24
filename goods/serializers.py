from rest_framework import serializers
from goods.models import ItemNew


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemNew
        fields = ['id', 'name', 'description', 'weight']
