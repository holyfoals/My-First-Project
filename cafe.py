# This program takes an existing menu and set of items and allows the user to add items to the menu,
# update any stock's amount i.e. how many have been sold in the day, and get a total of everything,
# in the cafe. 

menu = ["Espresso", "Cortado", "Flat White", "Latte", "Cappuccino"]

stock = {"Espresso": 13, "Cortado": 9, "Flat White": 23, "Latte": 25, "Cappuccino": 19}
price = {"Espresso": 2.10, "Cortado": 2.50, "Flat White": 2.90, "Latte": 3.10, "Cappuccino": 3.10}

# Function to calculate amount of stock and how much value it has
def total():
    total_stock = 0
    for items in menu:
        item_value = (stock[items] * price[items])
        print(f"{items} x{stock[items]} - Total: £{item_value:.2f}")
        total_stock += (stock[items] * price[items])
    print(f"\nThe total value, of all the stock in the cafe, is £{total_stock:.2f}")

# Function to print 'Current stock list' 
def stock_list():
    for key in stock.keys():
        print(f"{key} x{stock[key]} - £{price[key]:.2f} each")

# Function to print 'Updated stock list' with nice layout
def updated_stock_list():
    print("-" * 40)
    print("\t Updated Stock List \t")
    print("-"* 40)
    stock_list() 
    print("-" * 40)

# Start of program for the user
    
print("-" * 40)
print("\t Current Stock List \t")
print("-"* 40)
stock_list() 
print("-" * 40)

done = False

while (not done):
    choice = input(
'''
Would you like to:
A - Add item
B - Update stock level
C - Edit drink name and/or drink price
D - View total
E - Exit \n''').capitalize()

    if choice == "A":       # User can enetr what item they want to add to the menu, including how much it costs
        new_item = input("What item would you like to add: \n").title().strip()
            
        if new_item not in menu:
            menu.append(new_item)
            quantity = input("How many are currently in stock: \n")
            stock[new_item] = int(quantity)
            value = input("How much does the item cost: \n£")
            price[new_item] = float(value)

            updated_stock_list()
            print("-" * 40)
            print(f"{new_item} has been added to the menu with {quantity} added to stock list!")


        else:
            print("*Sorry, that item is already on the menu*", "\n", end="-"* 80)
    
    elif choice == "B":     # User can enter which item they want to update the stock for
        new_stock = input("What drink's stock level would you like to update: \n").title()
        if new_stock in menu:
            stock_level = input("Are you adding stock or decreasing stock: \n1 - Add stock\n2 - Decrease stock\n")
        
            if stock_level == "1":
                added_drinks = input("How many drinks are to be added: \n")
                stock[new_stock] += int(added_drinks)
                updated_stock_list()
                print("-" * 40)
                item_value = (stock[new_stock] * price[new_stock])
                print(f"The total value for {new_stock} is now £{item_value:.2f}")

            elif stock_level == "2":
                sold_drinks = input("How many drinks have been sold: \n")
                stock[new_stock] -= int(sold_drinks)
                updated_stock_list()
                print("-" * 40)
                item_value = (stock[new_stock] * price[new_stock])
                print(f"The total value for {new_stock} is now £{item_value:.2f}")
        else:
            print("\n*That drink isn't currently on the menu, please either check spelling or choose 'A' and add the new drink*", "\n" , end="-"* 80)

    elif choice == "C":
        edit = input(
'''
Would you like to update a drink's name, price or both: 
1 - Name
2 - Price
0 - Both \n''')
        
        if edit == "1":
            name_edit = input("Which drink's name needs editing: \n").title()
            if name_edit not in menu:
                print("*That drink isn't currently on the menu, please try again*", "\n" , end="-"* 80)
            else:
                new_name = input("What would you like to change the drink's name to: \n").title()
                for i in range(len(menu)):
                    if menu[i] == name_edit:
                        menu[i] = new_name

                stock[new_name] = stock.pop(name_edit)
                price[new_name] = price.pop(name_edit)
                updated_stock_list()
                print("-" * 40)
                print(f"'{name_edit}' has been updated to '{new_name}'")
            
        elif edit == "2":
            price_edit = input("Which drink needs the price updating: \n").title()
            if price_edit not in menu:
                print("\n*Error, that drink isn't currently on the menu, please try again*", "\n" , end="-"* 80) 
            else:
                new_price = float(input("What is the new price: \n£"))
                price[price_edit] = new_price
                updated_stock_list()
                print("-" * 40)
                print(f"{price_edit} now costs £{new_price:.2f}!")

        elif edit == "0":
            name_edit = input("Which drink's name needs editing: \n").title()
            if name_edit not in menu:
                print("*That drink isn't currently on the menu, please try again*", "\n" , end="-"* 80)
            else:
                new_name = input("What would you like to change the drink's name to: \n").title()
                new_price = float(input("What is the new price: \n£"))
                price[new_name] = new_price
                for i in range(len(menu)):
                    if menu[i] == name_edit:
                        menu[i] = new_name
                stock[new_name] = stock.pop(name_edit)
                price[new_price] = price.pop(name_edit)
                updated_stock_list()
        else:
            print("\n*Error, please choose a number*", "\n" , end="-"* 80)

    elif choice == "D":     # Make this option look nicer
        print("-"* 40)
        total()
        print("-" * 40)
    elif choice == "E":
        print("-"* 40)
        print("Thank you for using this stock tracker program :)")
        print("-" * 40)
        done = True
    else:
        print("Please enter a valid letter")











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