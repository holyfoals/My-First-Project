

menu = ["Espresso", "Cortado", "Flat White", "Latte", "Cappuccino"]

stock = {"Espresso": 13, "Cortado": 9, "Flat White": 23, "Latte": 25, "Cappuccino": 19}
price = {"Espresso": 2.10, "Cortado": 2.50, "Flat White": 2.90, "Latte": 3.10, "Cappuccino": 3.10}

# Function to calculate amount of stock and how much value it has
def total():
    total_stock = 0
    for items in menu:
        item_value = (stock[items] * price[items])
        print(f"The total value for {items} is £{item_value:.2f}")
        total_stock += (stock[items] * price[items])
    print(f"The total value, of all the stock in the cafe, is £{total_stock:.2f}")

# Code to print 'Current stock list' 
def stock_list():
    for key in stock.keys():
        print(f"{key} x{stock[key]} - £{price[key]:.2f} each")



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
C - View total
D - Exit \n''').capitalize()

    if choice == "A":
        new_item = input("What item would you like to add: \n").title()
        if new_item in menu:
            print("*Sorry, that item is already on the menu*", "\n", end="-"* 80)
            

        elif new_item not in menu:
            menu.append(new_item)
            quantity = input("How many are currently in stock: \n")
            stock[new_item] = int(quantity)
            value = input("How much does the item cost: \n£")
            price[new_item] = float(value)

            print("-" * 40)
            print("\t Updated Stock List \t")
            print("-"* 40)
            stock_list() 

    # Start of code to update stock and find out what stock item needs updating

    elif choice == "B":
        new_stock = input("What drink's stock level would you like to update: ").title()

        if new_stock in stock:
            drink = input("How many drinks have been sold: \n")
            stock[new_stock] -= int(drink)
            for key in stock.keys():
                print(key, "-", stock[key])
            item_value = (stock[new_stock] * price[new_stock])
            print(f"The total value for {new_stock} is now £{item_value:.2f}")
        else:
            print("*That drink isn't currently on the menu, please choose 'A' and add the new drink*", "\n" , end="-"* 80)
    elif choice == "C":
        total()
    elif choice == "D":
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