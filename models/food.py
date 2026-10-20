from models.product import Product


class Food(Product):
    expiry_date = ""

    def __init__(self, name, product_id, price, quantity, expiry_date):
        super().__init__(name, product_id, price, quantity)
        self.expiry_date = expiry_date

    def display_info(self):
        super().display_info()
        print("Expiry date:", self.expiry_date)

    # Backward compatibility alias
    def displey_info(self):
        self.display_info()

    def get_total_price(self, amount):
        total_price = super().get_total_price(amount)
        total_price += total_price * 0.1
        return total_price
