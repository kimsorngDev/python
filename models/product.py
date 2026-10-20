from exceptions import OutOfStockError, InvalidQuantityError


class Product:
    name = ""
    product_id = 0
    price = 0
    __quantity = 0

    def __init__(self, name, product_id, price, quantity):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    # Backward compatibility alias
    def get__quantity(self):
        return self.__quantity

    @property
    def quantity(self):
        return self.__quantity

    def restock(self, amount):
        if amount <= 0:
            raise InvalidQuantityError("Amount must be greater than 0")
        self.__quantity += amount

    def sell(self, amount):
        if amount <= 0:
            raise InvalidQuantityError("Amount must be greater than 0")
        if amount > self.__quantity:
            raise OutOfStockError("Out of stock")
        self.__quantity -= amount

    def get_total_price(self, amount):
        total_price = self.price * amount
        return total_price

    def display_info(self):
        print("Product name:", self.name)
        print("Product ID:", self.product_id)
        print("Price:", self.price)
        print("Quantity:", self.__quantity)
