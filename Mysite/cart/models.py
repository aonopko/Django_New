
from django.db import models
from app_admin.models import Item


class CartItem(models.Model):
    quantity = models.PositiveIntegerField(verbose_name="Описание")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="incart")
