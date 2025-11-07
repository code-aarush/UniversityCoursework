# Find the roots of a quadratic equation

import math

a = int(input("In the equation (ax^2 + bx + c) enter value of a: "))
b = int(input("In the equation (ax^2 + bx + c) enter value of b: " ))
c = int(input("In the equation (ax^2 + bx + c) enter value of c: " ))

D = b**2 - 4*a*c

if D >= 0:
    root1 = (-b + math.sqrt(D)) / (2 * a)
    root2 = (-b - math.sqrt(D)) / (2 * a)
    print(f"Roots are: {root1} and {root2}")
else:
    print("No real roots")
    