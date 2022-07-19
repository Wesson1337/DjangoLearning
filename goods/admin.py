from django.contrib import admin
from goods.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
