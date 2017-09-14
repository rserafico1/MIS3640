#Exercise 1 - Quadratic Function

import math

def quadratic(a,b,c):
    print('ax**2 + bx + c = 0' .format(a,b,c))
    discriminant = b**2-4*a*c
    if discriminant > 0: 
        x1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
        print('Two solutions')
        print(x1)
        print(x2)
    if discriminant == 0:
        x1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
        print('One solution')
        print(x1)
    if discriminant < 0:
            print('No solution')

def test():
    quadratic(1,5,6)

test()