"""
If the first number is greater than the second, 
print "The first number is greater". 
Otherwise, print "The first number is not greater".

If the two numbers are equal 
print "The numbers are equal".
 Otherwise, print "The numbers are not equal".

If the second number is greater than the first, 
print "The second number is greater". 
Otherwise, print "The second number is not greater".
"""

num1 = float(input("What is the first number?"))
num2 = float(input("What is the second number?"))

if num1 == num2:
    print("The first number is not greater")
    print("The numbers are equal")
    print("The second number is not greater")
elif num1 > num2:
    print("The first number is greater")
    print("The numbers are not equal")
    print("The second number is not greater")
else:
    print("The first number is not greater")
    print("The numbers are not equal")
    print("The second number is greater")

my_fav_animal = "bear"
you_fav_animal = input("What is your favorite animal?")

if my_fav_animal == you_fav_animal.lower():
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")