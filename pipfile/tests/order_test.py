from customer import Customer
from coffee import Coffee
from order import Order

def test_order_init():
    customer = Customer("Hank")
    coffee = Coffee("Iced Coffee")
    order = Order(customer, coffee, 4.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.5

def test_order_validation():
    customer = Customer("Ivy")
    coffee = Coffee("Cold Brew")
    
    try:
        Order(customer, coffee, "4.0")
        assert False
    except TypeError:
        pass
    
    try:
        Order(customer, coffee, 0.5)
        assert False
    except ValueError:
        pass

def test_order_immutability():
    customer = Customer("Jack")
    coffee = Coffee("Macchiato")
    order = Order(customer, coffee, 5.0)
    
    try:
        order.price = 6.0
        assert False
    except AttributeError:
        pass