from django.contrib import admin

from models import CartItem


@admin.register(CartItem)
class ItemAdmin(admin.ModelAdmin):
    pass



