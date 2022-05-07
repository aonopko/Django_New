from datetime import date

from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(null=True)


class Category(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Катеории'


class Item(models.Model):
    name = models.CharField(max_length=155)
    category = models.ManyToManyField(Category, )
    price = models.DecimalField(max_digits=15, decimal_places=3)
    quantity = models.IntegerField()
    img = models.ImageField(blank=True, upload_to="static/")

    def __str__(self):
        return self.category


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created = models.DateField(default=date.today)
    quantity = models.IntegerField()


class Cart(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='cart')
