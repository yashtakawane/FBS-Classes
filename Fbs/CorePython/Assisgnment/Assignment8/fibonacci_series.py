#Write a program to find print the following Fibonacci series using
#functions:
#1 1 2 3 5 8 n terms

def fibonacciSeries(n):
    a=1
    b=1
    for i in range(1 , n +1):
        c = a + b
        a=b
        b=c
        print(a , end = ' ')   #this is used to print in a single line instead of into multiple line
                
    return
n=int(input('Enter n:'))
res=fibonacciSeries(n)
print(f'The sum of fibonacci series till {n} is {res}')
