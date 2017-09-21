def factorial(n):
    result = 1
    if n == 1:
        return result 
    else:
        print('current n =', n)
        result = n * factorial(n-1)
        return result

print(factorial(10))
