class Product:
    """Represents a product in the store."""
    def __init__(self, name, price, quantity):
        """Initialize the product with name, price, and quantity."""
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        """Return the current quantity of the product."""
        return float(self.quantity)

    def set_quantity(self, quantity):
        """Set the quantity of the product."""
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Return whether the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self) -> str:
        """Return a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> None:
        """
        Purchase a specified quantity of the product.

        Args:
            quantity (int): The quantity of the product to purchase.

        Returns:
            float: The total cost of the purchase.

        Raises:
            ValueError: If the quantity is not positive or if there is not enough stock.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantity

