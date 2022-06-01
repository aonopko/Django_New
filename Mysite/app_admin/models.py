from datetime import date

from phonenumber_field.modelfields import PhoneNumberField

from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,
                            unique=True)
    email = models.EmailField(null=True)


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=155,
                            verbose_name="Название")
    category = models.ManyToManyField(Category,
                                      verbose_name="Категория" )
    price = models.DecimalField(max_digits=155,
                                decimal_places=3,
                                verbose_name="Цена")
    quantity = models.IntegerField(verbose_name="Количество")
    img = models.ImageField(blank=True, upload_to="static/")

    def get_categories(self):
        return [x.name for x in self.category.all()]


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='orders')
    created = models.DateField(default=date.today)
    quantity = models.IntegerField()


class Cart(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE,
                              related_name='cart')


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=155)
    massage = models.CharField(max_length=500)
