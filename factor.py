#1
#Factoring of integers. 
#Write a program that asks the user for an integer and then prints out all its factors. 
#For example, when the user enters 150, the program should print 2 3 5 5

#Works with 'Terminal', rather than 'Debug Console' 

# INSTRUCTIONS 
# 1. Run program on 'Terminal'
# 2. Enter integer 
# 3. List of factors will print

def print_factors(n):
    d = 2
    factors = [ ] #List of factors of input number 
    while n > 1:
        if n % d == 0: 
            factors.append(d) 
            n = n/d #Divide by 2 as much as possible
        else:
            d = d + 1 #Continue to divide until no more factors
    return factors
num = int(input("Please enter an integer:")) #Allows and tells user to enter integer
print(print_factors(num))