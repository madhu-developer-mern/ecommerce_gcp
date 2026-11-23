from decimal import Decimal
from django.db import transaction
from rest_framework import serializers
from products.models import Product
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'price', 'quantity', 'subtotal']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'full_name',
            'email',
            'phone',
            'address',
            'city',
            'state',
            'pin_code',
            'total_amount',
            'status',
            'created_at',
            'items'
        ]
        read_only_fields = ['id', 'user', 'total_amount', 'status', 'created_at']

class CreateOrderItemInputSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(required=True, min_value=1)

class CreateOrderSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(max_length=20, required=True)
    address = serializers.CharField(required=True)
    city = serializers.CharField(max_length=100, required=True)
    state = serializers.CharField(max_length=100, required=True)
    pin_code = serializers.CharField(max_length=20, required=True)
    items = CreateOrderItemInputSerializer(many=True, required=True)

    def validate_items(self, items):
        if not items:
            raise serializers.ValidationError("Order must include at least one item.")

        validated_items = []
        for item in items:
            product_id = item.get('product_id')
            quantity = item.get('quantity')

            try:
                product = Product.objects.get(id=product_id, is_active=True)
            except Product.DoesNotExist:
                raise serializers.ValidationError(f"Product with ID {product_id} does not exist or is inactive.")

            if product.stock < quantity:
                raise serializers.ValidationError(
                    f"Insufficient stock for '{product.name}'. Available: {product.stock}, requested: {quantity}."
                )

            validated_items.append({
                'product': product,
                'quantity': quantity
            })

        return validated_items

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user

        with transaction.atomic():
            # Calculate total strictly from database product prices
            total_amount = Decimal('0.00')
            order_items_to_create = []

            for item in items_data:
                # Select for update to safely protect against concurrent stock changes
                product = Product.objects.select_for_update().get(id=item['product'].id)
                quantity = item['quantity']

                if product.stock < quantity:
                    raise serializers.ValidationError(
                        f"Stock changed for '{product.name}'. Available: {product.stock}, requested: {quantity}."
                    )

                subtotal = product.price * quantity
                total_amount += subtotal

                # Deduct stock
                product.stock -= quantity
                product.save(update_fields=['stock'])

                order_items_to_create.append({
                    'product': product,
                    'product_name': product.name,
                    'price': product.price,
                    'quantity': quantity,
                    'subtotal': subtotal
                })

            # Create Order
            order = Order.objects.create(
                user=user,
                total_amount=total_amount,
                **validated_data
            )

            # Create Order Items
            for item_info in order_items_to_create:
                OrderItem.objects.create(
                    order=order,
                    product=item_info['product'],
                    product_name=item_info['product_name'],
                    price=item_info['price'],
                    quantity=item_info['quantity'],
                    subtotal=item_info['subtotal']
                )

        return order
