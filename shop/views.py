from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from django.views.generic import TemplateView

from shop.models import Product, FlowerCategory, Order, OrderItem, SubscriptionLog
# Create your views here.
class ShowFlowersView(TemplateView):
    template_name = "shop/show_flowers.html"

    def get_context_dara(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context["products"]=Product.objects.all()

        return context
