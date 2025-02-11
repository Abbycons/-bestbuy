from typing import List

class Product:
    """
    Represents a product in the store.
    Example implementation for resolving 'Product' reference.
    """
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def is_active(self) -> bool:
        return self.active and self.quantity > 0

    def get_quantity(self) -> int:
        return self.quantity

    def buy(self, amount: int) -> float:
        if amount <= 0 or amount > self.quantity:
            raise ValueError("Invalid purchase amount")
        self.quantity -= amount
        return amount * self.price


class Store:
    def __init__(self, product_list: List[Product]):
        """Initialize the store with a list of products."""
        self.products = product_list

    def add_product(self, product: Product):
        """Add a product to the store's inventory."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Remove a product from the store's inventory."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Return the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Return a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        """
        Process an order for a list of products and quantities.

        Args:
            shopping_list: A list of tuples containing products and their quantities.

        Returns:
            The total price of the order.

        Raises:
            ValueError: If a product in the shopping list is not available.
        """
        total_price = 0
        for product, quantity in shopping_list:
            if product in self.products and product.is_active():
                total_price += product.buy(quantity)
            else:
                raise ValueError(f"Product {product.name} is not available.")
        return total_price