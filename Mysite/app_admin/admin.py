from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Cart, Category, Order, Item


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'sub_name']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'image_show', 'get_categories']
    filter_horizontal = ('category', )

    def image_show(self, obj):
        if obj.img:
            return mark_safe(f'<img src= "{obj.img.url}" width="100" height="100"')
