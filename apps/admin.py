from django.contrib import admin

# from apps.models import Product
# @admin.register(Product)
# class StudentsModelAdmin(admin.ModelAdmin):
#     pass

from django.contrib import admin
from django.db import connection

from apps.models import Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save()

        with connection['django2'].cursor() as cursor:
            cursor.execute('INSERT INTO categories (name) VALUES (%s)', (obj.name,))

