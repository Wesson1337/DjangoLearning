from django.contrib import admin
from goods.models import Item, ItemNew


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(ItemNew)
class ItemNewAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']