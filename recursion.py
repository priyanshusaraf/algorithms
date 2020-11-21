#understanding recursion by 
#making a program that returns the 
#factorial of n

def sum(n):
  if n == 0:
    return 0

  prevSum = sum(n-1)
  return prevSum + n

print(sum(5))

#the fibonacci series
def fib(n):
  a = 0
  b = 1
  while a < n:  
    print(a, end=' ')
    a, b = b, a+b
    print()
fib(100)
