from django.db import models

# Create your models here.
class Customer(models.Model):
    full_name=models.TextField("ФИО")
    email=models.EmailField("Email")
    phone=models.TextField("Номер телефона")
    address=models.TextField("Адрес")

    class Meta:
        verbose_name="Клиент"
        verbose_name_plural="Клиенты"

class Order(models.Model):
    customer=models.ForeignKey("Customer", on_delete=models.CASCADE, null=True)
    date_order=models.DateTimeField("Дата заказа")
    delivery_date=models.DateTimeField("Дата доставки")
    status=models.TextField("Статус заказа")
    total_amount=models.DecimalField("Итоговая стоимость", max_digits=10, decimal_places=2)
    subscription=models.BooleanField("Подписка")
    sub_period=models.IntegerField("Период подписки")
    start_data=models.DateField("Дата начала подпсики")
    end_data=models.DateField("Дата окончания подписки")
    auto_renew=models.BooleanField("Автопродление")

    class Meta:
        verbose_name="Заказ"
        verbose_name_plural="Заказы"

    def __str__(self) -> str:
        return self.name


class SubscriptionLog(models.Model):
    order=models.ForeignKey("Order", on_delete=models.CASCADE, null=True)
    status=models.TextField("Статус падписки")
    date_order=models.DateField("Дата заказа")

    class Meta:
        verbose_name="Лог подписки"
        verbose_name_plural="Логи подписки"

    def __str__(self) -> str:
        return self.name

class OrderItem(models.Model):
    order=models.ForeignKey("Order", on_delete=models.CASCADE, null=True)
    product=models.ForeignKey("Product", on_delete=models.CASCADE, null=True)
    quantity=models.IntegerField("Количество")
    price=models.DecimalField("Цена", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name="Состав заказа"
        verbose_name_plural="Состав заказов"
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name=models.TextField("Название")
    category=models.ForeignKey("FlowerCategory", on_delete=models.CASCADE, null=True)
    price=models.DecimalField("Цена", max_digits=10, decimal_places=2)
    description=models.TextField("Описание")
    image=models.ImageField("Фото", null=True, upload_to='product')
    in_stock=models.BooleanField("Наличие")
    stock_quantity=models.IntegerField("Количество")
    is_subscription=models.BooleanField("Подписка")

    class Meta:
        verbose_name="Товар"
        verbose_name_plural="Товары"

    def __str__(self) -> str:
        return self.name

       
class FlowerCategory(models.Model):
    name=models.TextField("Название")
    description=models.TextField("Описание")
    season=models.TextField("Сезон")
    image=models.ImageField("Фото", null=True, upload_to='category')

    class Meta:
        verbose_name="Категория цветов"
        verbose_name_plural="Категории цветов"

    def __str__(self) -> str:
            return self.name