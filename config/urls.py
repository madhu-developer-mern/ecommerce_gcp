"""
URL configuration for SimpleShop backend.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """
    Health check API endpoint for Cloud Run and monitoring.
    """
    return Response({
        "status": "ok",
        "service": "simpleshop-backend"
    })

@api_view(['GET'])
@permission_classes([AllowAny])
def version_check(request):
    """
    Version check API endpoint for Cloud Run revision testing and canary deployments.
    """
    return Response({
        "version": "v2",
        "environment": "production",
        "service": "ecommerce-gcp"
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/health/', health_check, name='health-check'),
    path('api/version/', version_check, name='version-check'),
    path('api/auth/', include('users.urls')),
    path('api/products/', include('products.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/cart/', include('cart.urls')),
]
