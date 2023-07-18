class Restaurant:
    def __init__(self, name, address, contact_information):
        self.name = name
        self.address = address
        self.contact_info = contact_information
        self.menu = {}

    def add_menu(self, menu):
        self.menu = menu

    def remove_menu(self):
        self.menu = {}

    def update_menu(self, new_menu):
        self.menu = new_menu

    def get_menu(self):
        return self.menu


class Menu:
    def __init__(self):
        self._item = []

    def add_item(self, name, description, price):
        try:
            add = MenuItem(name, description, price)
            self._item.append(add)
            print("item added")
        except ValueError as e:
            print (e)

    def remove_item(self, item):
        if item in self._item:
            self._item.remove(item)
        else:
            print("your order is not in the menu")

    def update(self, item_name, new_name, new_description, new_price):
        for item in self._item:
            if item.get_name() == item_name:
                item.name = new_name
                item.description = new_description
                item.price = new_price
                break
        else:
            print("Your order is not in the menu")

    def get_item(self):
        return self._item


class MenuItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        if not isinstance(name, str):
            raise ValueError("name should be a string.")
        if not isinstance(description, str):
            raise ValueError("description should be a string.")
        if not isinstance(price, int):
            raise ValueError("price should be a full number.")

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price


class Customer:
    def __init__(self, name, address, contact_information):
        self._name = name
        self._address = address
        self._contact_info = contact_information
        self.order_history = []

    def place_order(self, items):
        order = Order(self, items)
        self.order_history.append(order)
        print("order placed.")

    def view_order_history(self):
        if len(self.order_history) == 0:
            print("sorry, you haven't any order history.")
        else:
            print("your order history:")
            for order in self.order_history:
                print(
                    "Order from: ",
                    order.get_restaurant_name(),
                    "restaurant & Total Price:",
                    order.get_total_price(),
                )


class Order:
    def __init__(self, customer, items, discount=""):
        self._customer = customer
        self._restaurant_name = None
        self._items = items
        self._total_price = self.calculate_total_price(discount)
        self._customer_discount = discount

    def set_restaurant_name(self, name):
        self._restaurant_name = name

    def get_restaurant_name(self):
        return self._restaurant_name

    def get_total_price(self):
        return self._total_price

    def calculate_total_price(self, discount=""):
        total_price = 0
        for item in self._items:
            total_price += item.get_price()
        return total_price - self.calculate_discount(discount)

    def calculate_discount(self, discount=""):
        if not isinstance(discount, str):
            raise ValueError("discount should be a string.")
        if discount[0:3] == "Low":
            # 20% discount
            result = self._total_price - (self._total_price * 0.2)
            return result
        elif discount[0:4] == "half":
            # 50% discount
            result = self._total_price - (self._total_price * 0.5)
            return result
        else:
            return 0


class OrderHistory:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def remove_order(self, order):
        self.orders.remove(order)

    def view_orders(self, order):
        for order in self.orders:
            print("Customer:", order.customer.name)
            print("Customer Address:", order.customer.address)
            print("Customer Contact Information:", order.customer.contact_info)
            print("Order from ", order.restaurant.name, "restaurant:")
            print("Restaurant Address:", order.restaurant.address)
            print("Restaurant Contact Information:", order.restaurant.contact_info)



def main():

    menu_item1 = MenuItem("Fried Chicken","Chicken fillet, French fries, Special sauce",250000)
    menu_item2 = MenuItem("Crispy Chicken", "Fried Chicken Breast, cheese, lettuce, pickles cucumber",200000)
    menu_item3 = MenuItem("chicken alfredo pizza","pizza dough, alfredo sauce, cheese, grilled chicken, sweet pepper",190000)
   
   
    menu_item4 = MenuItem("tachin","rice, meat, yogurt, eggs, saffron",180000)
    menu_item5 = MenuItem("gormeh sabzi", "a mix of kidney beans, meat, special herb, rice",120000)

    restaurant = Restaurant("Divan", "Tehran, Freshteh st, Sam center,5th floor", "22017534")

    restaurant.update_menu("Roberto", "Tehran, Pasdaran, Bostan 2", "02126701830")

    restaurant.add_menu("Cabbage salad",[menu_item1, menu_item2, menu_item3])
    restaurant.add_menu("Yogurt",[menu_item4, menu_item5])

    restaurant.get_menu()

