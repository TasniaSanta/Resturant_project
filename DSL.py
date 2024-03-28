class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.options = []

    def add_option(self, name, price):
        self.options.append({"name": name, "price": price})

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item_name, options=None):
        if options is None:
            options = []
        self.items.append({"name": item_name, "options": options})

class MenuDSL:
    def __init__(self):
        self.menu = []

    def item(self, name, price):
        self.menu.append(MenuItem(name, price))
        return self.menu[-1]

    def order(self, customer_name):
        return Order(customer_name)

    def display_menu(self):
        print("Menu:")
        for item in self.menu:
            print(f"{item.name}: ${item.price}")
            if item.options:
                print("Options:")
                for option in item.options:
                    print(f"- {option['name']}: ${option['price']}")
            print()

# Usage example:
dsl = MenuDSL()

# Define menu items
kilburn_chocolate_cake = dsl.item("cake", 12)
kilburn_chocolate_cake.add_option("Extra chocolate", 1)
kilburn_chocolate_cake.add_option("Fruit", 2)

dsl.item("Drinks", 5)
dsl.item("coffee", 8)

# Define orders
order1 = dsl.order("Tasnia santa")
order1.add_item("sunny_ao_cake", ["Choclate"])
order1.add_item("Drinks", ["Latta"])

order2 = dsl.order("Jane Smith")
order2.add_item("kilburn_chocolate_cake", ["Extra Choclate"])
order2.add_item("cappuccino")

order3 = dsl.order("Bob Johnson")
order3.add_item("queen_park_cake", ["Kiwi"])
order3.add_item("Latta")
order3.add_item("Latta")

# Display menu
dsl.display_menu()
