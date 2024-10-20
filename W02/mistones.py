"""""
Thais Rodrigues
Project 02 :  Meal Price Calculator

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

total = subtotal_meal + sales_tax
print(f"Total: $ {total:.2f}")

payment_amount = float(input("What is the payment amount?  "))
change = payment_amount - total
print(f"Change: $ {change:.2f}")