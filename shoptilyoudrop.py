#SHOP 'TIL YOU DROP! Game

from random import randint

getcontext().prec = 2
getcontext().rounding = ROUND_HALF_UP

class Product:
    def __init__(self, input_name, input_price, input_stock = 0):
        self.name = input_name
        self.price = input_price
        self.stock = input_stock

    def __repr__(self):
        string = "Product: " + self.name + ", has a stock of " + str(self.stock) + " units at a price of $" + str(round(float(self.price),2)) + " each."
        return string

    def sell_product(self, quantity):
        if quantity > self.stock:
            print("There are not enough units in stock.")
        else:
            self.stock -= quantity

    def price():
        return self.price


class Shopper:
    def __init__(self, input_name, input_products = []):
        self.name = input_name
        self.budget = 0
        self.products = input_products

    def __repr__(self):
        string = "The shopper: " + self.name + ", has a budget of $" + str(self.budget) + "."
        return string

    def assign_budget(self):
        budget = round(randint(1000, 2000),0)
        self.budget = budget
        print(f"\nYou have a budget of: ${self.budget}")

    def products_bought(self):
        for product in self.products:
            print(f"Product: {product.name}")

    def print_budget(self):
        print(f"{self.budget}")

    def print_balance(self):
        num_products = shopping_cart.num_products()
        total = 0
        for i in range(num_products):
            total += shopping_cart.qty[i] * shopping_cart.price[i]
        balance = self.budget - total
        difference = 100 - ((total / self.budget) * 100)
        if difference <= 10 and balance >= 0:
            print(f"Your balance is: $ {balance:.2f}")
            print(f"the difference is: {difference:.2f}%")
            print("You WON!!!\n")
            print("\n\n\n\n\n")

        else:
            print(f"Your balance is: $ {balance:.2f}")
            print(f"the difference is: {difference:.2f}%")
            print("You LOST!!!\n")
            print("\n\n\n\n\n")

        

class ShoppingCart:
    def __init__(self, input_product, input_qty, input_price):
        self.product = input_product
        self.qty = input_qty
        self.price = input_price

    def __repr__(self):
        string = "The cart has the following products: "
        return string

    def add_product(self, product, qty, price):
        self.product.append(product)
        self.qty.append(qty)
        self.price.append(float(price))
    
    def print_shopping_cart(self):
        print("\n-------------------------- \nShopping Cart: \n-------------------")
        for i in range(len(self.product)):
            stotal = self.qty[i] * self.price[i]
            print(f"{self.product[i]}, {self.qty[i]}, ${self.price[i]:.2f}, ${stotal:.2f}")
        print("\n--------------------------")

    def num_products(self):
        return len(self.product)

p1 = Product('p1', 19.42, 10)
p2 = Product('p2', 35.13, 50)
p3 = Product('p3', 27.46, 24)
p4 = Product('p4', 42.67, 96)
p5 = Product('p5', 14.89, 48)

# print(p1)
# print(p2)
# print(p3)
# print(p4)
# print(p5)

def print_products():
    print("\nProducts: \n-------------------")
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(p5)

shopper_1 = Shopper('shopper 1')

shopping_cart = ShoppingCart([], [], [])

# print(shopper_1)

def play_game():
    print("\nSHOP 'TIL YOU DROP! \n-------------------\n")
    print("Rules\n-------")
    print("The aim of the game is to buy products with all the budget assigned to you. At the end, If your balance is less than 10% of your budget, you WON.")
    print("You'll have a budget of $1000 to $2000 to buy products. Budget amount will be assigned randomly.")
    print("You can buy as many units as you want of each product.")
    print("At the beginning of the game, the stock of each product will be assigned randomly.")
    print("You have to buy at least one unit of each product.")
    print("If you want buy a quantity of units that exceed the stock an error message will appear.")
    print("BUT, if your shopping cart total exceeds your budget, you LOST.")
    shopper_1.assign_budget()
    print_products()


    while True:
        ptb = input("\nWhat product do you want to buy? (type e to end)")

        if ptb == '':
            print("\n\n\n\n\n")
            break

        if ptb == 'e':
            shopping_cart.print_shopping_cart()
            shopper_1.print_balance()
            break

        prd = eval(ptb)
        qtb = int(input("How many units do you want to buy? "))
        price = prd.price
        # print("input: " + str(prd.name) + " / " + str(qtb) + " / " + str(price))

        shopping_cart.add_product(prd.name, qtb, price)

        # shopper_1.print_budget()
        # if shopper_1.budget <= 0:
        #     print("You don't have enough money to buy more products.")
        #     break

play_game()
