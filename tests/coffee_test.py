from customer import Customer
from coffe import Coffee
from order import Order

def test_coffee_init():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_name_validation():
    try:
        Coffee(123)
        assert False
    except TypeError:
        pass
    
    try:
        Coffee("ab")
        assert False
    except ValueError:
        pass

def test_coffee_orders():
    coffee = Coffee("Mocha")
    customer = Customer("Dave")
    order = Order(customer, coffee, 6.0)
    assert order in coffee.orders()

def test_coffee_customers():
    coffee = Coffee("Americano")
    customer1 = Customer("Eve")
    customer2 = Customer("Frank")
    Order(customer1, coffee, 3.0)
    Order(customer2, coffee, 3.5)
    assert len(coffee.customers()) == 2

def test_coffee_methods():
    coffee = Coffee("Flat White")
    customer = Customer("Grace")
    Order(customer, coffee, 4.0)
    Order(customer, coffee, 4.5)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 4.25