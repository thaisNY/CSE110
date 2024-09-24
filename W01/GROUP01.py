import math

side_square = float(input("Type the length of side of square"))
radius = float(input("Type the length of the radius"))
base = float(input("Type the length of the base of a retangule"))
high = float(input("Type the length of a high of a rentangule"))

area_square = side_square ** 2
area_circle = math.pi * (radius** 2)
area_retangle = base * high

print(f"The area of the squere is: {area_square}")
print(f"The area of the circle is: {area_circle}")
print(f"The area of the retangule is: {area_retangle}")
