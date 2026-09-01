#Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n
#b. 1!+ 2! + 3! + 4!+..... + n!
#c. 1^1 + 2^2 + 3^3+ ...... n^n

def sumSeries(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum

def factorialSeries(n):
    fact=1
    sum=0
    for i in range(1,n+1):
        fact=fact*i
        sum=sum+fact
    return sum

def exponentialSeries(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i**i
    return sum

n=int(input('Enter the n end of the series'))
res1=sumSeries(n)
res2=factorialSeries(n)
res3=exponentialSeries(n)
print(f'The sum of series from 1 to {n} is {res1}')
print(f'The sum of factorial series from 1 to {n} is {res2}')
print(f'The sum of exponential series from 1 to {n} is {res3}')

