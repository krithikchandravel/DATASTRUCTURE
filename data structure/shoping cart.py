class Shopping_cart:
    items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def show_cart(self):
        return self.items


cart = Shopping_cart()


cart.add_item(input("enter item:"))
cart.add_item(input("enter item:"))


print("Current cart items:", cart.show_cart())

cart.remove_item(input("enter item to remove:"))


print("Updated cart items:", cart.show_cart())
