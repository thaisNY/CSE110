import math
size1 = float(input("Type the size in centimeters"))

area_square = size1 ** 2
area_circle = math.pi * (size1 ** 2)
volume_cube = size1 ** 3

print(f"The area of square in centimeter is {area_square} cm")
print(f"The area of square  is {area_square / 100} meters")

print(f"The area of circle in centimeter is {area_circle} cm")
print(f"The area of circle  is {area_circle / 100} meters")

print(f"The volume of cube in centimeter is {volume_cube} cm")
print(f"The volume of cube is {volume_cube / 100} meters")
 
 