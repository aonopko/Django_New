from django.contrib import admin

from .models import Cart, Category, Order, Item


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
