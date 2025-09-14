#	Write a program that takes the radius as input and calculates the area and circumference of a circle.
import math
radius = float(input("Enter the radius of the circle: "))

area = math.pi * (radius**2)
circumference = 2 * math.pi * radius 

print("Area of the circle is: ", area)
print("Circumference of the Circle is: ", circumference)