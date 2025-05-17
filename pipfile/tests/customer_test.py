from pipfile.customer import Customer
from pipfile.coffe import Coffee
from pipfile.order import Order

def test_customer_init():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_name_validation():
    try:
        Customer(123)
        assert False
    except TypeError:
        pass
    
    try:
        Customer("")
        assert False
    except ValueError:
        pass

def test_customer_orders():
    customer = Customer("Bob")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert order in customer.orders()

def test_customer_coffees():
    customer = Customer("Charlie")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Cappuccino")
    Order(customer, coffee1, 4.0)
    Order(customer, coffee2, 5.0)
    Order(customer, coffee1, 4.5)
    assert len(customer.coffees()) == 2