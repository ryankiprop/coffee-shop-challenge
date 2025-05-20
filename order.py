from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customer import Customer
    from coffe import Coffee

class Order:
    all = []

    def __init__(self, customer: 'Customer', coffee: 'Coffee', price: float):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price: float):
        if not isinstance(price, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        if hasattr(self, '_price'):
            raise AttributeError("Price cannot be changed after initialization")
        self._price = price

    @property
    def customer(self) -> 'Customer':
        return self._customer

    @customer.setter
    def customer(self, customer: 'Customer'):
        from customer import Customer  # Local import to avoid circular dependency
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be an instance of Customer class")
        self._customer = customer

    @property
    def coffee(self) -> 'Coffee':
        return self._coffee

    @coffee.setter
    def coffee(self, coffee: 'Coffee'):
        from coffe import Coffee  # Local import to avoid circular dependency
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be an instance of Coffee class")
        self._coffee = coffee