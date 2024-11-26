
import os
from datetime import datetime
from logging import root
from multiprocessing import Value
from unicodedata import category

import django
from django.db.models import F, Sum

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

django.setup()

from apps.models import Product, Category, _User

# s='texnika'
# a = Product.objects.filter(name__icontains=s).values('name').annotate(model_name=Value('name'))
# b = Category.objects.filer(name__icontains=s).values('name').annotate(model_name=Value('name'))
# c = a.union(b)
# for i in c:
#     print(i.name)
#
# p = Product.objects.extra(name__icontains=s)
# for i in Category.objects.all():
#     print(i.name==s)

# StudentsModel.objects.exclude(category='Electronica')
#
# StudentsModel.objects.exclude(pub_date__gt=datetime.date(2005, 1, 3), headline="Hello")


# d = Product.objects.get(id=1)
# b = Product.objects.get(id=1)
# print(b.name)
# for _ in b:
#     print(_)


# obj, created = Product.objects.get_or_create(
#     category__name__="meva",
#     Product="banan",
#     create_defaults={"first_name": "banana", "price": 25000},
# )

# p = Product.objects.filter(Q(category__name='meva')| Q(category__name='banan')).update(price=25_000)
#
# pc = Product.objects.filter(Q(category__name='meva')| Q(category__name='banan')).update(price=25_000)


#
# print(Product.objects.in_bulk([1, 2],field_name = 'id'))
#
# print(Product.objects.distinct("name").in_bulk(['Banan', 'Banana'],field_name="name"))

# results = Product.objects.values(c_name=F('category__name'))
# for i in results:
#     print(i)


# results = Product.objects.values(c_name=F('category__name')).annotate(sum=Sum("price"))
# for result in results:
#     print(result)


# vowels = "aeiouAEIOU"
#
# last_users = _User.objects.all().order_by('-date_joined')[:1]
#
# products = Product.objects.filter(
#     owner__in=last_users,
#     name__regex=r'^[aeiouAEIOU]'
# )
#
# print(products.update(price=F('price') + 1000))
#
# res = Product.objects.filter('price')[2000:3500]

filtered_products = Product.objects.filter(
    price__gte=2000,
    price__lte=3500,

    description__isnull=False,
    description__exact='',
    name__icontains='a'
)

for product in filtered_products:
    print(f"Name: {product.name}, Price: {product.price}, Description: {product.description}")
