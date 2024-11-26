from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.models import Product, Category


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 10
    def get_queryset(self):
        return Product.objects.all()


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    paginate_by = 10
    def get_queryset(self):
        return Category.objects.all()

class TopishVaChiqarish(ListView):
    s = 'texnika'
    model1 = Product.objects.all()
    model2 = Category.objects.all()
    context_object_name = 'proandcat'
    paginate_by = 10
    def get_queryset(self):
        pass

