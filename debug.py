from coffe import Coffee
from customer import Customer
from order import Order

def main():
    print("☕ Coffee Shop System Debug ☕\n")
    
    # Create some coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    cappuccino = Coffee("Cappuccino")
    
    # Create customers
    alice = Customer("Alice")
    bob = Customer("Bob")
    
    # Create orders
    print("Creating orders...")
    order1 = Order(alice, latte, 4.5)
    order2 = Order(alice, espresso, 3.0)
    order3 = Order(bob, cappuccino, 5.0)
    order4 = Order(bob, latte, 4.0)
    print("Orders created successfully!")
    
    # Test relationships
    print(f"\n{alice.name}'s orders:")
    for order in alice.orders():
        print(f"- {order.coffee.name}: ${order.price}")
    
    print(f"\n{latte.name} customers:")
    for customer in latte.customers():
        print(f"- {customer.name}")
    
    # Test methods
    print(f"\n{latte.name} stats:")
    print(f"- Orders: {latte.num_orders()}")
    print(f"- Avg price: ${latte.average_price():.2f}")
    
    # Test create_order
    new_order = bob.create_order(espresso, 3.5)
    print(f"\nNew order created: {new_order.coffee.name} for ${new_order.price}")

if __name__ == "__main__":
    main()