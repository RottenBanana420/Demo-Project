class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def checkout(self):
        total_price = sum(item["product"].price * item["quantity"] for item in self.items)
        return total_price
