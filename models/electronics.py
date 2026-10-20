from models.product import Product


class Electronics(Product):
    warranty_months = ""

    def __init__(self, name, product_id, price, quantity, warranty_months):
        super().__init__(name, product_id, price, quantity)
        self.warranty_months = warranty_months

    def display_info(self):
        super().display_info()
        print("Warranty months:", self.warranty_months)

    # Backward compatibility alias
    def displey_info(self):
        self.display_info()

    def get_total_price(self, amount):
        total_price = super().get_total_price(amount)
        total_price = total_price * 1.05
        return total_price