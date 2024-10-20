"""
Showing creativite
1- The output of prices has 2 decimals cases
2- Show the quantity of items

"""

print("Welcome to the Shopping Cart Program!")

items = []
prices = []
item = None
price = 0
ans = 0
count = 0

while ans != 5:
    print("""Please select one of the following: 
    1. Add item
    2. View cart
    3. Remove item
    4. Compute total
    5. Quit""")

    ans = int(input("Please enter an action: "))

    if ans == 1:
        count += 1
        item = input("What item would you like to add?")
        items.append(item)
        price = float(input(f"What is the price of {item} ?"))
        prices.append(price)
        print(f"{item} has been added to the cart.")
        print(f"At the moment the list has {count} items")
    elif ans == 2:
        print("The contents of the shopping cart are:")
        for i in range (len(items)):
            items[i]
            prices[i]
            print(f"{i + 1}. {items[i]}  -- ${prices[i]:.2f}")
        print(f"At the moment the list has {count} items")
            
    elif ans == 3:
        count -= 1
        print("The contents of the shopping cart are:")
        for i in range (len(items)):
            items[i]
            prices[i]
            print(f"{i + 1}. {items[i]}  -- ${prices[i]:.2f}")

        item_remove = int(input("Which item would you like to remove?"))
        index_remove = item_remove - 1
        items.pop(index_remove)
        prices.pop(index_remove)
        print("Item removed")
    elif ans == 4:
        total = 0
        for i in range (len(prices)):
            total += prices[i]
        print(f"The total price of the items in the shopping cart is $ {total}")
        
print("Thank you. Goodbye.")
    