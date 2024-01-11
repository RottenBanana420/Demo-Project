class User:
    def __init__(self, name, address, card_details):
        self.name = name
        self.address = address
        self.card_details = card_details
        self.cart = Cart()

    def view_catalogue(self, catalogue):
        print("Catalogue:")
        for product in catalogue:
            print(f"{product.product_id}. {product.name} - ${product.price}")

    def continue_shopping(self):
        response = input("Do you want to continue shopping? (yes/no): ")
        return response.lower() == "yes"
