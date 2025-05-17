from pipfile.customer import Customer
from pipfile.coffe import Coffee
from pipfile.order import Order

def main():
    print("☕ Coffee Shop Debug Console ☕\n")

    # Test Customer
    print("1. Testing Customer:")
    alice = Customer("Alice")
    print(f"- Created customer: {alice.name}")

    try:
        Customer(123)
    except TypeError:
        print("- Caught error when using number for name")

    try:
        Customer("")
    except ValueError:
        print("- Caught error when name is too short")

    alice.name = "Alice W"
    print(f"- Changed name to: {alice.name}")

    # Test Coffee
    print("\n2. Testing Coffee:")
    latte = Coffee("Latte")
    print(f"- Created coffee: {latte.name}")

    try:
        Coffee("Te")
    except ValueError:
        print("- Caught error when coffee name is too short")

    try:
        latte.name = "New Latte"
    except AttributeError:
        print("- Caught error when trying to change coffee name")

    # Test Orders
    print("\n3. Testing Orders:")
    bob = Customer("Bob")
    espresso = Coffee("Espresso")
    cappuccino = Coffee("Cappuccino")

    order1 = Order(bob, espresso, 3.5)
    order2 = Order(bob, cappuccino, 4.0)
    print(f"- Created 2 orders for Bob")

    print("\n4. Testing Relationships:")
    print(f"- Bob's orders: {[o.coffee.name for o in bob.orders()]}")
    print(f"- Bob's unique coffees: {[c.name for c in bob.coffees()]}")
    print(f"- Espresso has {espresso.num_orders()} orders")
    print(f"- Espresso average price: ${espresso.average_price():.2f}")

    # Test create_order method
    print("\n5. Testing create_order:")
    charlie = Customer("Charlie")
    mocha = Coffee("Mocha")
    charlie.create_order(mocha, 4.5)
    print(f"- Charlie ordered {mocha.name} for $4.50")

    # Test edge cases
    print("\n6. Testing Edge Cases:")
    new_coffee = Coffee("New Brew")
    print(f"- {new_coffee.name} has {new_coffee.num_orders()} orders")

    new_customer = Customer("Newbie")
    print(f"- {new_customer.name} has ordered {len(new_customer.coffees())} coffees")

if __name__ == "__main__":
    main()