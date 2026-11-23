from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer

class ProductListAPIView(generics.ListAPIView):
    """
    GET /api/products/
    Returns all active products.
    Supports query parameters:
      - search: searches name and description
      - category: filters by category
    """
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)

        search = self.request.query_params.get('search', '').strip()
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )

        category = self.request.query_params.get('category', '').strip()
        if category and category.lower() != 'all':
            queryset = queryset.filter(category__iexact=category)

        return queryset

class ProductDetailAPIView(generics.RetrieveAPIView):
    """
    GET /api/products/<id>/
    Returns product details.
    """
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
