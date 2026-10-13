from django.contrib import admin

from shop.models import Customer, Order

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['full_name', 'email', 'phone', 'address' ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass





