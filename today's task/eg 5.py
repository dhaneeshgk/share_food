def fib(n):

   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))

item = 3

if item <= 0:
  print("Plese enter a +ve integer")
else:
 for i in range(item+1):
       print(fib(i))
