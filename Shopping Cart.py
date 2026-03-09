class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self):
        name = input("Item name: ")
        price = float(input("Item price: "))
        self.cart.append(Item(name, price))
        print("Item added\n")

    def remove_item(self):
        name = input("Item name to remove: ")
        for item in self.cart:
            if item.name == name:
                self.cart.remove(item)
                print("Item removed\n")
                return
        print("Item not found\n")

    def view_cart(self):
        if not self.cart:
            print("Cart is empty\n")
        else:
            print("Here's your shopping cart:")
            for item in self.cart:
                print(item.name, "-", item.price)
            print()

    def checkout(self):
        if not self.cart:
            print("Cart is empty\n")
            return
        print("===== Checkout =====")
        for item in self.cart:
            print(item.name, "-", item.price)
        print("--------------------")
        print("Total:", sum(item.price for item in self.cart))
        print("====================\n")

cart = ShoppingCart()
print("===== Shopping Cart Menu =====")
while True:
    print("1 Add\n2 Remove\n3 View\n4 Checkout\n5 Exit")
    choice = input("Choose: ")
    if choice == "1":    cart.add_item()
    elif choice == "2":  cart.remove_item()
    elif choice == "3":  cart.view_cart()
    elif choice == "4":  cart.checkout()
    elif choice == "5":  break