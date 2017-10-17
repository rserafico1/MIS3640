#Question 1
def replace_even(data):
    '''
    Replace all elements at an even index in the list with 0.
    No return is required.
    data: the list of values to process'''
    for i, n in enumerate(data): 
        if n % 2 != 0:
            data[i] = 0
    

# Uncomment the following lines to test
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
replace_even(ONE_TEN)
print(ONE_TEN) #Answer 1

# Expected output:
# [0, 2, 0, 4, 0, 6, 0, 8, 0, 10]

#Question 2
def remove_middle(data):
    '''
    Remove the middle element if the list length is odd,
    or the middle two elements if the list length is even.  
    No return is required.
    data: the list of values to process
    '''
    for i, n in enumerate(data): 
        if n % 2 == 0:
            del data[4:-4]
        else:
            del data[4:2]

# Uncomment the following lines to test
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_middle(ONE_TEN)
print(ONE_TEN) #Answer 2

# Expected output:
# [1, 2, 3, 4, 7, 8, 9, 10]


#Question 3
def insert_integer(data, number):
    '''
    given a sorted list of integers, insert a new integer into
    its proper position so that the new list stays sorted. 
    Do not use sort function or sorted function inside this function.
    data: a list of integers
    number: a new integer
    return: a new list of sorted integers with previous numbers and 
    the new number
    '''
    #data = [1, 3, 40, 75, 90, 2000, 2001, 2016]
    #number = 2015
    #for i in range(len(data)):
    #    if data[i] > number:
    #        index = i
    #        break
    #insert_integer = data[:i] + [number] + data[i:]
    for n in range(0, len(data)):
        if (data[n] >= number):
            data.insert(n, number)
            break
    return data

#import bisect
#data = [1, 3, 40, 75, 90, 2000, 2001, 2016]
#number = 2015
#bisect.insort(data, 2015)
#print(data) #Answer 3

# Uncomment the following lines to test
data = [1, 3, 40, 75, 90, 2000, 2001, 2016]
new_data = insert_integer(data, 2015)
print(new_data)

# Expected output:
# [1, 3, 40, 75, 90, 2000, 2001, 2015, 2016]

#Question 4
def print_hist(data):
    '''
    given a dictionary of letter: positive integer pairs, 
    print rows with the letter and a number of asterisks equal
    to the positive integer. The rows should be printed in key order.
    No return is required.
    data: a dictionary of letter: positive integer pairs
    Example:
    letter_counts={'C': 6, 'A': 3, 'B': 10, 'Z': 8}
    print_hist(letter_counts)
    Expected output:
    A: ***
    B: **********
    C: ******
    Z: ********
    '''
    for x in sorted(data):
        g = data[x]
        print(x, ":", g*'*')  

letter_counts={'C': 6, 'A': 3, 'B': 10, 'Z': 8}
print_hist(letter_counts) #Answer 4