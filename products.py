class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        return float(self.quantity)

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
            return self.price * quantity