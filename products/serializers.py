from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'category',
            'price',
            'stock',
            'image_url',
            'is_active',
            'created_at',
            'updated_at'
        ]
