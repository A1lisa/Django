from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from shop.models import Product, OrderItem, Order, Customer, SubscriptionLog, FlowerCategory
from shop.serializers import ProductSerializer, OrderItemSerializer, OrderSerializer, CustomerSerializer, SubscriptionLogSerializer, FlowerCategorySerializer

class ProductViewSet(mixins.CreateModelMixin, 
                    mixins.UpdateModelMixin, 
                    mixins.RetrieveModelMixin, 
                    mixins.DestroyModelMixin, 
                    mixins.ListModelMixin, 
                    GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderItemViewSet(mixins.CreateModelMixin, 
                    mixins.UpdateModelMixin, 
                    mixins.RetrieveModelMixin, 
                    mixins.DestroyModelMixin, 
                    mixins.ListModelMixin, 
                    GenericViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderViewSet(mixins.CreateModelMixin, 
                    mixins.UpdateModelMixin, 
                    mixins.RetrieveModelMixin, 
                    mixins.DestroyModelMixin, 
                    mixins.ListModelMixin, 
                    GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class FlowerCategoryViewSet(mixins.CreateModelMixin, 
                    mixins.UpdateModelMixin, 
                    mixins.RetrieveModelMixin, 
                    mixins.DestroyModelMixin, 
                    mixins.ListModelMixin, 
                    GenericViewSet):
    queryset = FlowerCategory.objects.all()
    serializer_class = FlowerCategorySerializer

class CustomerViewSet(mixins.CreateModelMixin, 
                    mixins.UpdateModelMixin, 
                    mixins.RetrieveModelMixin, 
                    mixins.DestroyModelMixin, 
                    mixins.ListModelMixin, 
                    GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SubViewSet(mixins.CreateModelMixin, 
                    mixins.UpdateModelMixin, 
                    mixins.RetrieveModelMixin, 
                    mixins.DestroyModelMixin, 
                    mixins.ListModelMixin, 
                    GenericViewSet):
    queryset = SubscriptionLog.objects.all()
    serializer_class = SubscriptionLogSerializer
    
    