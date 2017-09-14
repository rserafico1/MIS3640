def print_lyrics(): 
    print("Hey Jude. Don't Make it bad.")
    print("Take a sad song and made it better.")

print_lyrics()

print(type(print_lyrics))

def repeat_lyrics(): 
    print_lyrics()
    print('Na - na - na - na - na - na - na - na')
    print_lyrics()

repeat_lyrics()

def print_twice(name):
    print(name)
    print(name)

print_twice('Rey')

my_name = 'Regine'
print_twice(my_name)


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