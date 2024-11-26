# from django.db.models import Model, ForeignKey, CASCADE, Manager, QuerySet
# from django.db.models import CharField, IntegerField
# from rest_framework.fields import DateTimeField, BooleanField
#
#
# class _User(Model):
#     full_name = CharField(max_length=100)
#     join_at = DateTimeField()
#
# class Category(Model):
#     name = CharField(max_length=255)
#
# class ProductManager(Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_premium=True)
#
# class ProductQuerySet(QuerySet):
#     def top_products(self):
#         return self.filter(is_premium=True, price__gt=15000)
#
# class Product(Model):
#     name = CharField(max_length=50)
#     price = IntegerField()
#     is_premium = BooleanField(default=False)
#     is_deleted = BooleanField(default=False)
#     objects = ProductManager.from_queryset(ProductQuerySet)()
#
#
# print(Product.objects.filter(ProductQuerySet))
# Product.objects.top_products()
#

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name