from models.food import Food
from models.electronics import Electronics
from models.product import Product
from models.shop import Shop

shop = Shop()

while True:
    print("=========================================")
    print("SHOP MENU")
    print("=========================================")

    print("1. add food product")
    print("2. add electronics product")
    print("3. Restock product")
    print("4. Sell product")
    print("5. Show all products")
    print("6. Show low stock products")
    print("7. Show total sales")
    print("8. Remove products")
    print("9. Exit")

    menu = input("Enter your choice: ")

    match menu:
        case "1":
            try:
                name = input("Enter name: ")
                product_id = input("Enter product_id: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                expiry_date = input("Enter expiry_date: ")

                food = Food(name, product_id, price, quantity, expiry_date)
                shop.add_product(food)
                print("Successfully!!")
            except ValueError as e:
                print(f"Error: {e}")

        case "2":
            try:
                name = input("Enter name: ")
                product_id = input("Enter product_id: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                warranty_months = input("Enter warranty months: ")

                electronics = Electronics(name, product_id, price, quantity, warranty_months)
                shop.add_product(electronics)
                print("Successfully!!")
            except ValueError as e:
                print(f"Error: {e}")

        case "3":
            try:
                product_id = input("Enter product id: ")
                product = shop.find_product(product_id)
                if product is None:
                    print("Product not found!")
                else:
                    amount = int(input("Enter restock quantity: "))
                    product.restock(amount)
                    print("Product restocked successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        case "4":
            try:
                product_id = input("Enter product id: ")
                amount = int(input("Enter product quantity: "))

                total_price = shop.sell_product(product_id, amount)
                print(f"Total price: ${total_price:.2f}")
                print("Successfully!!")
            except Exception as e:
                print(f"Error: {e}")

        case "5":
            shop.show_all_products()

        case "6":
            try:
                limit = int(input("Enter low-stock limit: "))
                products = shop.get_low_stock(limit)

                if products:
                    for product in products:
                        product.display_info()
                        print("--------------------------")
                else:
                    print("No low-stock products found.")
            except ValueError as e:
                print(f"Error: {e}")

        case "7":
            print("Total sales: $", shop.total_sales())

        case "8":
            try:
                product_id = input("Enter product ID to remove: ")
                shop.remove_product(product_id)
                print("Product removed successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        case "9":
            print("Thank you for using the Shop Manager!")
            break

        case _:
            print("Invalid!!")
