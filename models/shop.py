from exceptions import ProductNotFoundError, ProductAlreadyExistsError


class Shop:
    def __init__(self):
        self.products = {}
        self.sales_history = []

    # 1. Add product
    def add_product(self, product):
        if product.product_id in self.products:
            raise ProductAlreadyExistsError("Product ID already exists")

        self.products[product.product_id] = product

    # 2. Find product
    def find_product(self, product_id):
        return self.products.get(product_id)

    # 3. Remove product
    def remove_product(self, product_id):
        if product_id not in self.products:
            raise ProductNotFoundError("Product not found")

        del self.products[product_id]

    # 4. Sell product
    def sell_product(self, product_id, amount):
        product = self.find_product(product_id)

        if product is None:
            raise ProductNotFoundError("Product not found")

        product.sell(amount)

        total_price = product.get_total_price(amount)

        sale = {
            "product_id": product_id,
            "amount": amount,
            "total_price": total_price
        }

        self.sales_history.append(sale)
        return total_price

    # 5. Show all products
    def show_all_products(self):
        if not self.products:
            print("No products available.")
            return

        for product in self.products.values():
            product.display_info()
            print("----------------------")

    # 6. Get low-stock products
    def get_low_stock(self, limit):
        low_stock_products = []

        for product in self.products.values():
            if product.get_quantity() <= limit:
                low_stock_products.append(product)

        return low_stock_products

    # 7. Calculate total sales
    def total_sales(self):
        total = 0

        for sale in self.sales_history:
            total += sale["total_price"]

        return total