import json

class OrderManager:
    def __init__(self, filename="order_records.json"):
        self.filename = filename

    def save_order(self, order):
        with open(self.filename, 'a') as file:
            json.dump(order.to_dict(), file)
            file.write('\n')

    def view_all_orders(self):
        try:
            with open(self.filename, 'r') as file:
                orders = file.readlines()
                for idx, order in enumerate(orders, start=1):
                    print(f"Order {idx}:\n{order}")
        except FileNotFoundError:
            print("No orders found.")
