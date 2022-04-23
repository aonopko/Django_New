from datetime import date

from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(null=True)


class Category(models.Model):
    name = models.CharField(max_length=255)
    sub_name = models.CharField(max_length=150)


class Item(models.Model):
    name = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=3)
    quantity = models.IntegerField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created = models.DateField(default=date.today)
    quantity = models.IntegerField()
    cart = models.OneToOneField('Cart', on_delete=models.CASCADE)


class Cart(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='cart')
