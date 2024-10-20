"""""
Thais Rodrigues
Project 02 :  Meal Price Calculator

Enhancements:
1. Added the tip to total only if you eat at the restaurant
2. Added to option to dilevery or pickup, for delivery there is a delivery tax

"""

child_meal = float(input("What is the price of a child's meal?  "))
adult_meal = float(input("What is the price of an adult's meal?  "))
number_children = int(input("How many children are there?  "))
number_adult = int(input("How many adults are there?  "))
subtotal_meal = (child_meal * number_children) + (adult_meal * number_adult)
print(f"Subtotal: ${subtotal_meal:.2f}")


sales_tax_rate = float(input("What is the sales tax rate?  "))
sales_tax = (subtotal_meal * sales_tax_rate)/100
print(f"Sales Tax: ${sales_tax:.2f}")


while True: 
    ans = input("Do you want delivery?(y/n)")
    if ans == 'y':
        DELIVERY_TAX = 20
        total = subtotal_meal + sales_tax + DELIVERY_TAX
        print(f"Total: $ {total:.2f}")
        break
    elif ans == 'n':
        bill = subtotal_meal + sales_tax
        tip = bill * 0.1
        total = bill + tip
        print(f"Total: $ {total:.2f}")
        break
    else:
        print("No valid answers")

payment_amount = float(input("What is the payment amount?  "))
change = payment_amount - total
print(f"Change: $ {change:.2f}")