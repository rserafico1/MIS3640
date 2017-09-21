def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))

ns = 10

if ns <= 0:
   print("Enter Integer")
else:
   print("Fibonacci sequence:")
   for i in range(ns):
       print(fib(i))