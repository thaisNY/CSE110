items_shop = []
item_shop = None
while item_shop != "quit" :
    item_shop = input("Please enter the items of the shopping " +
                   "list (type: quit to finish):")
    items_shop.append(item_shop)
    #print(f"Item:  {item_shop}")
items_shop.pop()
print("The shopping list is:")

for i in range(len(items_shop)):
    print(f"Item: {items_shop[i]}")

print("The shopping list with indexes is:")

for i in range(len(items_shop)):
    print(f" {i}. Item: {items_shop[i]}")

change = int(input("Which item would you like to change?"))
new_item = input("What is the new item?")
print("The shopping list with indexes is:")
for i in range(len(items_shop)):
    if i == change:
        items_shop[i] = new_item
    print(f" {i}. Item: {items_shop[i]}")




