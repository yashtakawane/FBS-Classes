#WAP to print Fibonacci series upto n.
n = int(input('Enter the number of series:'))
a= int(input('Enter a: '))
b = int(input('Enter b: '))
for i in range(1 , n +1):
    c = a + b
    print(c , end = ' ')   #this is used to print in a single line instead of into multiple line
    a=b
    b=c