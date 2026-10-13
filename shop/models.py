from django.db import models

# Create your models here.
class Customer(models.Model):
    full_name=models.CharField("ФИО")
    email=models.EmailField("Email")
    phone=models.CharField("Номер телефона")
    address=models.TextField("Адрес")

    class Meta:
        verbose_name="Клиент"
        verbose_name_plural="Клиенты"

class Order(models.Model):
    customer=models.ForeignKey("Customer", on_delete=models.CASCADE, null=True)
    date_order=models.DateTimeField("Дата заказа")
    delivery_date=models.DateTimeField("Дата доставки")
    status=models.CharField("Статус заказа")
    total_amount=models.DecimalField("Итоговая стоимость")
    subscription=models.BooleanField("Подписка")
    sub_period=models.IntegerField("Период подписки")
    start_data=models.DateField("Дата начала подпсики")
    end_data=models.DateField("Дата окончания подписки")
    auto_renew=models.BooleanField("Автопродление")

    class Meta:
            verbose_name="Заказ"
            verbose_name_plural="Заказы"
    

class SubscriptionLog(models.Model):
    order=models.ForeignKey("Order", on_delete=models.CASCADE, null=True)
    status=models.CharField("Статус падписки")
    date_order=models.DateField("Дата заказа")

    class Meta:
                verbose_name="Лог подписки"
                verbose_name_plural="Логи подписки"


class OrderItem(models.Model):
    order=models.ForeignKey("Order", on_delete=models.CASCADE, null=True)
    Product=models.ForeignKey("Product", on_delete=models.CASCADE, null=True)
    quantity=models.IntegerField("Количество")
    price=models.DecimalField("Цена")

    class Meta:
                verbose_name="Состав заказа"
                verbose_name_plural="Состав заказов"


class Product(models.Model):
       name=models.CharField("Название")
       category=models.ForeignKey("FlowerCategory", on_delete=models.CASCADE, null=True)
       price=models.DecimalField("Цена")
       description=models.TextField("Описание")
       image=models.ImageField("Фото")
       in_stock=models.BooleanField("Наличие")
       stock_quantity=models.IntegerField("Количество")
       is_subscription=models.BooleanField("Подписка")

       class Meta:
              verbose_name="Товар"
              verbose_name_plural="Товары"

class FlowerCategory(models.Model):
       name=models.CharField("Название")
       descroption=models.TextField("Описание")
       season=models.CharField("Сезон")
       image=models.ImageField("Фото")

       class Meta:
              verbose_name="Категория цветов"
              verbose_name_plural="Категории цветов"