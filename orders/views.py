from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer, CreateOrderSerializer

class CreateOrderView(APIView):
    """
    POST /api/orders/
    Create a new order. Authentication required.
    Validates product stock, calculates prices server-side,
    and decrements stock in an atomic transaction.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CreateOrderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            order = serializer.save()
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyOrdersView(generics.ListAPIView):
    """
    GET /api/orders/my-orders/
    Returns orders belonging only to the authenticated user.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related('items')
