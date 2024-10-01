class Shopping_cart:
    def _init_(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def show_cart(self):
        return self.items

# Create an instance of the Shopping_cart class
cart = Shopping_cart()

# Add items to the cart
cart.add_item("laptop")
cart.add_item("apple")

# Display the current cart contents
print("Current cart items:", cart.show_cart())

# Remove an item from the cart
cart.remove_item("apple")

# Display the updated cart contents
print("Updated cart items:", cart.show_cart())
