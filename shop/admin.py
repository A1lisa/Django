from django.contrib import admin

from shop.models import Customer, Order, FlowerCategory, Product, SubscriptionLog, OrderItem    

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id', 'full_name', 'email', 'phone', 'address' ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
     list_display=['id', 'customer', 'date_order', 'delivery_date', 'status', 'total_amount', 'subscription', 'sub_period', 'start_data', 'end_data', 'auto_renew']    

  
@admin.register(FlowerCategory)
class FlowerCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "season")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "in_stock", "stock_quantity", "is_subscription")

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "quantity", "price")


@admin.register(SubscriptionLog)
class SubscriptionLogAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "status", "date_order")
