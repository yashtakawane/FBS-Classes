#4. Write a program to find sum of n numbers using recursion.

def sumSeries(n):
    if n==0:
        return 0 
    else:
        return n + sumSeries(n-1)

n=int(input('Enter the number:'))
res=sumSeries(n)
print(res)