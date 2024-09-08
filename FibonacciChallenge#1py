list=[]
def fibonacci(n):
     #handel the the negative input
     if n < 0  :
          print('Please enter a valid positive integer!')
          return -1
     
     #base case to stop the recarsion
     if n==0 or n==1:
          return n
     
     #recarsive case 
     return fibonacci(n-1) +fibonacci(n-2)


try:
     num=int(input('enter a positive integer: '))
     n_fib=fibonacci(num)
     print(f'fibonacci {num} is {n_fib}')
     
except ValueError:
     #if the use enter a non-integer number
     print('Please enter a valid integer!')
