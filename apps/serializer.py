from apps.models import Product, Category
from rest_framework.serializers import ModelSerializer
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = 'name', 'slug'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'name', 'slug', 'uuid'
