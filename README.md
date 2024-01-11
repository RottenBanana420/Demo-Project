# Python Online Store

A simple online store implemented in Python with Object-Oriented Programming (OOP) principles. The application allows users to browse a catalog of items, add items to their cart, and proceed to checkout.

## Features

- **View Catalog:** Users can view the catalog of products with details such as name and price.
- **Add to Cart:** Users can add items to their cart with the option to specify the quantity.
- **Checkout:** Users can proceed to checkout with the items in their cart, providing address and card details.
- **Order History:** Order details are stored in a file, and users can view all the orders placed.

## Project Structure

- `main.py`: Main entry point for the application.
- `product.py`: Contains the Product class representing the products in the catalog.
- `user.py`: Contains the User class representing the users of the online store.
- `cart.py`: Contains the Cart class representing the user's shopping cart.
- `order.py`: Contains the Order class representing the details of an order.
- `order_manager.py`: Contains the OrderManager class responsible for saving and viewing orders.

## Usage

1. Run `main.py` to start the application.
2. Follow the prompts to browse the catalog, add items to the cart, and complete the checkout process.
3. Orders are stored in the `order_records.json` file.
