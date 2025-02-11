from products import Product
from store import Store

# Setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=50),
    Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = Store(product_list)


def list_products(store):
    """List all products in the store."""
    print("\nProducts in store:")
    for product in store.get_all_products():
        print(product.show())


def show_total_quantity(store):
    """Show the total quantity of items in the store."""
    total_amount = store.get_total_quantity()
    print(f"\nTotal amount in store: {total_amount} items")


def make_order(store):
    """Process an order for a selected product and quantity."""
    print("\nAvailable products:")
    for i, product in enumerate(store.get_all_products()):
        print(f"{i + 1}. {product.show()}")

    try:
        product_index = int(input("Select the product number: ")) - 1
        quantity = int(input("Enter the quantity: "))

        selected_product = store.get_all_products()[product_index]
        total_price = selected_product.buy(quantity)

        if total_price > 0:
            print(f"Order successful! Total price: ${total_price:.2f}")
        else:
            print("Order failed. Please check the product availability.")

    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid product number and quantity.")


def start(store):
    """
    Start the store interface and handle user interactions.

    Args:
        store (Store): The Store object representing the store's inventory.
    """
    while True:
        print("\nWelcome to Best Buy!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose an option (1-4): ")

        if choice == "1":
            list_products(store)
        elif choice == "2":
            show_total_quantity(store)
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Thank you for shopping with us. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")


# Start the program
start(best_buy)