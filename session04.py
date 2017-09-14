# Class Exercises on 9/12

print(13 % 5)
print(13 % 2)
print(13 // 2)
print(13 //5) 

type(42)
type(42.0)

round(3.85)
round(234.2342, 2)
min(8,3,9,1)
ord('a')
chr(97)

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