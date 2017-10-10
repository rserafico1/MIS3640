#2
#Write a recursive function isPalindrome(string) that returns True if string is a palindrome, that is, a word that is the same when reversed.
#Examples of palindromes are “deed”, “rotor”, or “aibohphobia”. 
#Hint: A word is a palindrome if the frst and last letters match and #the remainder is also a palindrome.


#Works with 'Terminal', rather than 'Debug Console' 

# INSTRUCTIONS 
# 1. Run program on 'Terminal'
# 2. Enter string 
# 3. "That's a palindrome" or "That isn't a palindrome" will print

def isPalindrome(s):
    length=len(s) #Number of elements in string input is 'length'
    if length < 2: 
        return print("That's a palindrome.")
    elif s[0] != s[-1]: #If the first element does not equal to the last element
        return print("That isn't a palindrome.")
    else:
        return isPalindrome(s[1:length - 1]) 

s = input("Enter a string: ") #Allows and tells user to enter a string
isPalindrome(s)
