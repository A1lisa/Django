from rest_framework import serializers
from shop.models import Product, Customer, OrderItem, Order, FlowerCategory, SubscriptionLog

class FlowerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowerCategory
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    category = FlowerCategorySerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'description', 'image', 'in_stock', 'stock_quantity', 'is_subscription']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
            model = Customer
            fields = ['id', 'full_name', 'email', 'phone', 'address']

class OrderSerializer(serializers.ModelSerializer):
    customer=CustomerSerializer(read_only=True)
    class Meta:
            model = Order
            fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
     Order=OrderSerializer(read_only=True)
     product=ProductSerializer(read_only=True)

     class Meta:
          model=OrderItem
          fields="__all__"
class SubscriptionLogSerializer(serializers.ModelSerializer):
     order=OrderSerializer(read_only=True)

     class Meta:
          model=SubscriptionLog
          fields="__all__"

