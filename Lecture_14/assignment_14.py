# Task 1
"""
Create a class Product with properties:
- name, 
- price, 
- quantity. 

Create a child class Book that:
- inherits from Product 
- adds:
	- a property author
	- a method called read that prints information about the book.
"""


class Product:
    # Adding custom attributes
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    # Adding custom attributes
    def __init__(self, name: str, price: int, quantity: int, author: str,):
        super().__init__(name, price, quantity)
        self.author = author
    
    def read(self):
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")


# Task 2
"""
Create a class Restaurant with properties:
- name,
- cuisine,
- menu
	- The menu property should be a dictionary with:
		- keys - dish name
        - values - price, (quantity)
     
Create a child class FastFood that:
- inherits from Restaurant

- adds:
	- a property drive_thru 
		- (a boolean indicating whether the restaurant has a drive-thru or not) 
    - a method called order which:
        - takes in:
            - the dish name
            - quantity 
        - returns:
            - the total cost of the order. 
        - update the menu dictionary:
            - subtract the ordered quantity from the available quantity. 
        - IF the dish is not available OR the requested quantity > available quantity:
            - THEN method should return a message indicating that the order cannot be fulfilled. Example of usage:
"""


class Restaurant:
    # Adding custom attributes
    def __init__(self, name: str, cuisine: str, menu: dict[str, dict[str, int]]):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


menu =  {
    'burger': {'price': 5, 'quantity': 10},
    'cheeseburger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15},
}

class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru: bool):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru
    

    def order(self, order_name: str, order_quantity: int):
        if order_name in self.menu:
            menu_quantity = self.menu[order_name]["quantity"]
            if menu_quantity > order_quantity:
                self.menu[order_name]["quantity"] -= order_quantity
                return order_quantity*self.menu[order_name]["price"]
            else:
                return f"'{order_name}' order quantity '{order_quantity}' exceeds available quantity '{menu_quantity}'."
        else:
            return f"Dish '{order_name}' is not available"


if __name__ == "__main__":
    # pass
    # Task 1
    # book_1 = Book("Apple of love", 13, 5, "Volodymyr Bananiv")
    # book_1.read()

    # Task 2
    mc = FastFood('McDonalds', 'Fast Food', menu, True)
    print(mc.menu["cheeseburger"])
    print(f'[ORDER] {mc.order("cheeseburger", 2)}')
    print(f'Updated menu: {mc.menu["cheeseburger"]}')
    print(f'[ORDER] {mc.order("cheeseburger", 9)}')
    print(f'[ORDER] {mc.order("snake", 9)}')

    # Task 3 - Optional
    # Coming soon
