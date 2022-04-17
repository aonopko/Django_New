from datetime import date

from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(null=True)


class Item(models.Model):
    item_name = models.ForeignKey('Category', on_delete=models.CASCADE)
    item_price = models.DecimalField(max_digits=15, decimal_places=3)
    item_quantity = models.IntegerField()


class Order(models.Model):
    order_number = models.ManyToManyField(User)
    order_data = models.DateField(default=date.today)
    order_quantity = models.IntegerField()
    order_item_name = models.ManyToManyField(Item)


class Category(models.Model):
    cat_name = models.CharField(max_length=150)
    sub_cat_name = models.CharField(max_length=150)
