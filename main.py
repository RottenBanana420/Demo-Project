from product import Product
from user import User
from order_manager import OrderManager
from order import Order
from cart import Cart

def get_valid_address():
    while True:
        address = input("Enter your address: ")
        if address:
            return address
        else:
            print("Please enter a valid address.")

def get_valid_card_details():
    while True:
        card_details = input("Enter your card details: ")
        if card_details:
            return card_details
        else:
            print("Please enter valid card details.")

def main():
    catalogue = [
        Product(1, "Product A", 20.0),
        Product(2, "Product B", 30.0),
        Product(3, "Product C", 25.0),
    ]

    user_name = input("Enter your name: ")
    user_address = get_valid_address()
    user_card_details = get_valid_card_details()

    user = User(user_name, user_address, user_card_details)

    while True:
        user.view_catalogue(catalogue)

        product_id = int(input("Enter the product ID to add to the cart (0 to exit): "))
        if product_id == 0:
            break

        try:
            selected_product = next(product for product in catalogue if product.product_id == product_id)
            quantity = int(input("Enter the quantity: "))
            user.cart.add_to_cart(selected_product, quantity)
        except StopIteration:
            print("Invalid product ID. Please try again.")

    total_price = user.cart.checkout()

    print(f"\nTotal price: ${total_price:.2f}")

    print("\nOrder placed successfully!")
    print("Acknowledgement:")
    print(f"Name: {user.name}")
    print(f"Address: {user_address}")
    print(f"Card Details: {user_card_details}")
    print("Items in Cart:")
    for item in user.cart.items:
        print(f"{item['product'].name} - Quantity: {item['quantity']}")
    print(f"Total Price: ${total_price:.2f}")

    order_manager = OrderManager()
    order = Order(user, user.cart.items, total_price, user_address, user_card_details)
    order_manager.save_order(order)

    view_orders = input("Do you want to view all orders? (yes/no): ")
    if view_orders.lower() == "yes":
        order_manager.view_all_orders()

if __name__ == "__main__":
    main()
