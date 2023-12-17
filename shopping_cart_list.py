# This program allows the user to shop in a pet food store.
# They can add and remove items from their cart, view the total cost and checkout

# Creating the 'stock' list of items the user can pick from

stock_list = ["Eggs", "Bread", "Oat Milk", "Haribo", "Cat Food", "Beef", "Ham"]


cart = []
prices = []
total = 0

menu = """Here are your choices:
1. Add an item to your cart
2. Remove an item from your cart
3. Checkout
4. Exit the shop"""

print("\n")
print("Welcome to Sumo's Shop!")
print("*" * 80)
print("Available items: ")
count = 1
for item in stock_list:                 # Loop to show available items in stock and able to add to the cart
    print(f"Item {count}: \t {item}")
    count += 1
done = False

while (not done):
    
    print("-" * 60)
    print("""Here is your shopping cart:
Item \t \t Price """)
    for i in range(len(cart)):          # Loop to print out any items that occur in both cart and prices
        print(f"{cart[i]} \t \t £{prices[i]:.2f}")
        if choice == "1":
            print(f"{cart[i]} has been added to the cart!")
    
    print("-" * 30)
    print(f"Cart Total: \t £{total:.2f}")
    print("-" * 60)
    print(menu)
    choice = input("What choice would you like: ")

    if choice == "1":
        item = input("What would you like to add to your cart: ").title()
        amount = int(input("How many: "))
        cost = float(input("How much does the item cost: £"))
        if item in stock_list:
            cart.append(item)
            cost *= amount
            prices.append(cost)
            total += cost
        else:
            print("Not available!")
        

        
    elif choice == "2":     # Removing items from the cart
        remove = input("What item would you like to remove: ").title()
        if remove in cart:
                index = cart.index(remove)
                cart.remove(remove)
                prices.pop(index)
        else:
            print("Thats not in your cart")

    elif choice == "4":     # Pulling together total 
        print("checkout")
        for i in range(len(cart)):          # Loop to print out any items that occur in both cart and prices
            print(f"{cart[i]} \t \t £{prices[i]:.2f}")
            print(total)

    elif choice == "5":
        print("")
        print("Thank you for shopping at Sumo's Shop <3")
        done = True

