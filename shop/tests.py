from itertools import product

from django.test import TestCase
from rest_framework.test import APIClient
from model_bakery import baker

from shop.models import Product, FlowerCategory, Customer, Order, OrderItem, SubscriptionLog

# Create your tests here.
class ProductViewsetTestCase(TestCase):
    def setUp(self):
        self.client=APIClient()

    """ def test_get_list(self):
        cat=FlowerCategory.objects.create( 
            name="Розы",
            description="",
            season="Лето",
            image=None,
        )

        product=Product.objects.create(
            name="Белые розы",
            category=cat,
            price="100.00",
            description="Описание",
            image=None,
            in_stock=True,
            stock_quantity=4,
            is_subscription=False,
        
        )
        r=self.client.get('/api/Product/')
        data=r.json()
        print(data)

        assert product.name == data[0]['name']
        assert product.id==data[0]['id']
        assert product.category.id==data[0]['category']
        assert len(data)==1 """

    def test_get_list(self):
        cat = baker.make("shop.FlowerCategory")
        product = baker.make("shop.Product", category=cat)

        r = self.client.get('/api/Product/')
        data = r.json()
        print(data)

        assert product.name == data[0]['name']
        assert product.id == data[0]['id']
        assert product.category.id == data[0]['category']
        assert len(data) == 1
    

    def test_create_product(self):
       """  cat=FlowerCategory.objects.create( 
                name="Розы",
                description="",
                season="Лето",
                image=None,
            ) """
       cat = baker.make("shop.FlowerCategory")
       r=self.client.post("/api/Product/",{
          "name" : "Красные розы",
          "category": cat.id,
          "price":"130.00",
          "description":"Красные",
          "in_stock":True,
          "stock_quantity":10,
          "is_subscription":False,
        })
       
       new_product_id=r.json()['id']

       products=Product.objects.all()
       assert len(products)==1

       new_product=Product.objects.filter(id=new_product_id).first()
       assert new_product.name=='Красные розы'
       assert new_product.category==cat
       assert new_product.price==130.00
       assert new_product.description=='Красные'
       assert new_product.in_stock==True
       assert new_product.stock_quantity==10
       assert new_product.is_subscription==False 

    def test_delete_product(self):
        products=baker.make("Product", 10)
        r=self.client.get("/api/Product/")
        data = r.json()
        assert len(data)==10

        product_id_to_delete=products[3].id
        self.client.delete(f'/api/Product/{product_id_to_delete}/')

        r=self.client.get('/api/Product/')
        data=r.json()
        assert len(data)==9

        assert product_id_to_delete not in [i['id'] for i in data]

    def test_update_product(self):
       cat = baker.make("shop.FlowerCategory")
       products = baker.make("shop.Product", category=cat, _quantity=10)
       product = products[2]
       
       r = self.client.get(f'/api/Product/{product.id}/')
       data = r.json()
       assert data['name'] == product.name

       r = self.client.put(f'/api/Product/{product.id}/', {
        "name": "Обновлённые розы",
        "category": product.category.id,
        "price": "150.00",
        "description": "Обновлённое описание",
        "in_stock": True,
        "stock_quantity": 5,
        "is_subscription": False,
        })
       assert r.status_code == 200

       r = self.client.get(f'/api/Product/{product.id}/')
       data = r.json()
       assert data['name'] == "Обновлённые розы"

       product.refresh_from_db()
       assert data['name'] == product.name

class FlowerCategoryViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        cat = baker.make("shop.FlowerCategory")

        r = self.client.get('/api/FlowerCategory/')
        data = r.json()
        print(data)

        assert cat.name == data[0]['name']
        assert cat.id == data[0]['id']
        assert len(data) == 1

    def test_create(self):
        r = self.client.post("/api/FlowerCategory/", {
            "name": "Тюльпаны",
            "description": "Весенние цветы",
            "season": "Весна",
        })

        new_id = r.json()['id']

        categories = FlowerCategory.objects.all()
        assert len(categories) == 1

        new_cat = FlowerCategory.objects.filter(id=new_id).first()
        assert new_cat.name == 'Тюльпаны'
        assert new_cat.season == 'Весна'

    def test_delete(self):
        categories = baker.make("shop.FlowerCategory", 10)

        r = self.client.get('/api/FlowerCategory/')
        data = r.json()
        assert len(data) == 10

        cat_id_to_delete = categories[3].id
        self.client.delete(f'/api/FlowerCategory/{cat_id_to_delete}/')

        r = self.client.get('/api/FlowerCategory/')
        data = r.json()
        assert len(data) == 9

        assert cat_id_to_delete not in [i['id'] for i in data]

    def test_update(self):
        categories = baker.make("shop.FlowerCategory", 10)
        cat = categories[2]

        r = self.client.get(f'/api/FlowerCategory/{cat.id}/')
        data = r.json()
        assert data['name'] == cat.name

        r = self.client.put(f'/api/FlowerCategory/{cat.id}/', {
            "name": "Пионы",
            "description": "Обновлённое описание",
            "season": "Лето",
        })
        assert r.status_code == 200

        r = self.client.get(f'/api/FlowerCategory/{cat.id}/')
        data = r.json()
        assert data['name'] == "Пионы"

        cat.refresh_from_db()
        assert data['name'] == cat.name


class CustomerViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        customer = baker.make("shop.Customer")

        r = self.client.get('/api/Customer/')
        data = r.json()
        print(data)

        assert customer.full_name == data[0]['full_name']
        assert customer.id == data[0]['id']
        assert len(data) == 1

    def test_create(self):
        r = self.client.post("/api/Customer/", {
            "full_name": "Иван Иванов",
            "email": "ivan@example.com",
            "phone": "+79001234567",
            "address": "Москва, ул. Ленина 1",
        })

        new_id = r.json()['id']

        customers = Customer.objects.all()
        assert len(customers) == 1

        new_customer = Customer.objects.filter(id=new_id).first()
        assert new_customer.full_name == 'Иван Иванов'
        assert new_customer.email == 'ivan@example.com'

    def test_delete(self):
        customers = baker.make("shop.Customer", 10)

        r = self.client.get('/api/Customer/')
        data = r.json()
        assert len(data) == 10

        customer_id_to_delete = customers[3].id
        self.client.delete(f'/api/Customer/{customer_id_to_delete}/')

        r = self.client.get('/api/Customer/')
        data = r.json()
        assert len(data) == 9

        assert customer_id_to_delete not in [i['id'] for i in data]

    def test_update(self):
        customers = baker.make("shop.Customer", 10)
        customer = customers[2]

        r = self.client.get(f'/api/Customer/{customer.id}/')
        data = r.json()
        assert data['full_name'] == customer.full_name

        r = self.client.put(f'/api/Customer/{customer.id}/', {
            "full_name": "Пётр Петров",
            "email": "petr@example.com",
            "phone": "+79007654321",
            "address": "Санкт-Петербург",
        })
        assert r.status_code == 200

        r = self.client.get(f'/api/Customer/{customer.id}/')
        data = r.json()
        assert data['full_name'] == "Пётр Петров"

        customer.refresh_from_db()
        assert data['full_name'] == customer.full_name


class OrderViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        order = baker.make("shop.Order")

        r = self.client.get('/api/Order/')
        data = r.json()
        print(data)

        assert order.id == data[0]['id']
        assert len(data) == 1

    def test_create(self):
        customer = baker.make("shop.Customer")

        r = self.client.post("/api/Order/", {
            "customer": customer.id,
            "date_order": "2025-01-15T10:00:00Z",
            "delivery_date": "2025-01-16T12:00:00Z",
            "status": "Новый",
            "total_amount": "2500.00",
            "subscription": False,
            "sub_period": 0,
            "start_data": "2025-01-15",
            "end_data": "2025-01-15",
            "auto_renew": False,
        })

        new_id = r.json()['id']

        orders = Order.objects.all()
        assert len(orders) == 1

        new_order = Order.objects.filter(id=new_id).first()
        assert new_order.customer == customer
        assert new_order.status == 'Новый'

    def test_delete(self):
        orders = baker.make("shop.Order", 10)

        r = self.client.get('/api/Order/')
        data = r.json()
        assert len(data) == 10

        order_id_to_delete = orders[3].id
        self.client.delete(f'/api/Order/{order_id_to_delete}/')

        r = self.client.get('/api/Order/')
        data = r.json()
        assert len(data) == 9

        assert order_id_to_delete not in [i['id'] for i in data]

    def test_update(self):
        customer = baker.make("shop.Customer")
        orders = baker.make("shop.Order", customer=customer, _quantity=10)
        order = orders[2]

        r = self.client.get(f'/api/Order/{order.id}/')
        data = r.json()
        assert data['id'] == order.id

        r = self.client.put(f'/api/Order/{order.id}/', {
            "customer": order.customer.id,
            "date_order": "2025-02-01T10:00:00Z",
            "delivery_date": "2025-02-02T12:00:00Z",
            "status": "Доставлен",
            "total_amount": "3000.00",
            "subscription": False,
            "sub_period": 0,
            "start_data": "2025-02-01",
            "end_data": "2025-02-01",
            "auto_renew": False,
        })
        assert r.status_code == 200

        r = self.client.get(f'/api/Order/{order.id}/')
        data = r.json()
        assert data['status'] == "Доставлен"

        order.refresh_from_db()
        assert data['status'] == order.status


class OrderItemViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        item = baker.make("shop.OrderItem")

        r = self.client.get('/api/OrderItem/')
        data = r.json()
        print(data)

        assert item.id == data[0]['id']
        assert len(data) == 1

    def test_create(self):
        order = baker.make("shop.Order")
        product = baker.make("shop.Product")

        r = self.client.post("/api/OrderItem/", {
            "order": order.id,
            "product": product.id,
            "quantity": 3,
            "price": "500.00",
        })

        new_id = r.json()['id']

        items = OrderItem.objects.all()
        assert len(items) == 1

        new_item = OrderItem.objects.filter(id=new_id).first()
        assert new_item.order == order
        assert new_item.product == product
        assert new_item.quantity == 3

    def test_delete(self):
        items = baker.make("shop.OrderItem", 10)

        r = self.client.get('/api/OrderItem/')
        data = r.json()
        assert len(data) == 10

        item_id_to_delete = items[3].id
        self.client.delete(f'/api/OrderItem/{item_id_to_delete}/')

        r = self.client.get('/api/OrderItem/')
        data = r.json()
        assert len(data) == 9

        assert item_id_to_delete not in [i['id'] for i in data]

    def test_update(self):
        order = baker.make("shop.Order")
        product = baker.make("shop.Product")
        items = baker.make("shop.OrderItem", order=order, product=product, _quantity=10)
        item = items[2]

        r = self.client.get(f'/api/OrderItem/{item.id}/')
        data = r.json()
        assert data['id'] == item.id

        r = self.client.put(f'/api/OrderItem/{item.id}/', {
            "order": item.order.id,
            "product": item.product.id,
            "quantity": 7,
            "price": "750.00",
        })
        assert r.status_code == 200

        r = self.client.get(f'/api/OrderItem/{item.id}/')
        data = r.json()
        assert data['quantity'] == 7

        item.refresh_from_db()
        assert data['quantity'] == item.quantity


class SubscriptionLogViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        log = baker.make("shop.SubscriptionLog")

        r = self.client.get('/api/Subscription/')
        data = r.json()
        print(data)

        assert log.id == data[0]['id']
        assert len(data) == 1

    def test_create(self):
        order = baker.make("shop.Order")

        r = self.client.post("/api/Subscription/", {
            "order": order.id,
            "status": "Активна",
            "date_order": "2025-01-15",
        })

        new_id = r.json()['id']

        logs = SubscriptionLog.objects.all()
        assert len(logs) == 1

        new_log = SubscriptionLog.objects.filter(id=new_id).first()
        assert new_log.order == order
        assert new_log.status == 'Активна'

    def test_delete(self):
        logs = baker.make("shop.SubscriptionLog", 10)

        r = self.client.get('/api/Subscription/')
        data = r.json()
        assert len(data) == 10

        log_id_to_delete = logs[3].id
        self.client.delete(f'/api/Subscription/{log_id_to_delete}/')

        r = self.client.get('/api/Subscription/')
        data = r.json()
        assert len(data) == 9

        assert log_id_to_delete not in [i['id'] for i in data]

    def test_update(self):
        order = baker.make("shop.Order")
        logs = baker.make("shop.SubscriptionLog", order=order, _quantity=10)
        log = logs[2]

        r = self.client.get(f'/api/Subscription/{log.id}/')
        data = r.json()
        assert data['id'] == log.id

        r = self.client.put(f'/api/Subscription/{log.id}/', {
            "order": log.order.id,
            "status": "Отменена",
            "date_order": "2025-02-01",
        })
        assert r.status_code == 200

        r = self.client.get(f'/api/Subscription/{log.id}/')
        data = r.json()
        assert data['status'] == "Отменена"

        log.refresh_from_db()
        assert data['status'] == log.status


