class Order:
    def __init__(self, user, items, total_price, address, card_details):
        self.user = user
        self.items = items
        self.total_price = total_price
        self.address = address
        self.card_details = card_details

    def to_dict(self):
        return {
            "user": self.user.name,
            "items": [{"product": item['product'].name, "quantity": item['quantity']} for item in self.items],
            "total_price": self.total_price,
            "address": self.address,
            "card_details": self.card_details
        }
