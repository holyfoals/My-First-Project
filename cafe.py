

menu = ["Espresso", "Cortado", "Flat White", "Latte", "Cappuccino"]

stock = {"Espresso": 13, "Cortado": 9, "Flat White": 23, "Latte": 25, "Cappuccino": 19}
price = {"Espresso": 2.10, "Cortado": 2.50, "Flat White": 2.90, "Latte": 3.10, "Cappuccino": 3.10}

# Code to print 'Current stock list' 
def stock_list():
    for key in stock.keys():
        print(f"{key} - {stock[key]} - £{price[key]:.2f}")

# Function to calculate amount of stock and how much value it has
def total():
    total_stock = 0
    for items in menu:
        item_value = (stock[items] * price[items])
        print(f"The total value for {items} is £{item_value:.2f}")
        total_stock += (stock[items] * price[items])
    print(f"The total value, of all the stock in the cafe, is £{total_stock:.2f}")

print("-" * 40)
print("\t Current Stock List \t")
print("-"* 40)
stock_list()

done = False

while (not done):
    choice = input(
'''
Would you like to:
A - Add item
B - Update stock
C - Exit \n''')

    if choice == "A":
        new_item = input("What item would you like to add: ").title()
        if new_item in menu:
            print("*Sorry, that item is already on the menu*")
            

        elif new_item not in menu:
            menu.append(new_item)
            value = input("How many are currently in stock: ")
            stock[new_item] = int(value)
            print("-" * 40)
            print("\t Updated Stock List \t")
            print("-"* 40)
            stock_list() 

    # Start of code to update stock and find out what stock item needs updating

    elif choice == "B":
        new_stock = input("What drink's stock level would you like to update: ")

        if new_stock.title() == "Espresso":
            drink = input("How many drinks have been sold: ")
            stock["Espresso"] -= int(drink)
            for key in stock.keys():
                print(key, "-", stock[key])
            item_value = (stock["Espresso"] * price["Espresso"])
            print(f"The total value for {menu[0]} is £{item_value:.2f}")

        elif new_stock.title() == "Cortado":
            drink = input("How many Cortado are there: ")
            stock["Cortado"] = int(drink)
            total()

        elif new_stock.title() == "Flat White":
            drink = input("How many Flat White are there: ")
            stock["Flat White"] = int(drink)
            total()

        elif new_stock.title() == "Latte":
            drink = input("How many Latte are there: ")
            stock["Latte"] = int(drink)
            total()
        elif new_stock.title() == "Cappuccino":
            drink = input("How many Cappuccino are there: ")
            stock["Cappuccino"] = int(drink)
            total()
       
    elif choice == "C":
        done = True
    else:
        print("invalid")










# item_value = 0
# drink = ""
# for key in stock:
#     item_value = stock[key] * price[key]
#     print(item_value)
# for drink in menu:
#     print(drink, item_value)
    

# """
# for each espresso
# it costs 2.10 and theres 13 of them

# """