#Write a program to find factorial using recursion.

def fact(n,f):
    if n==0:
        return f
    else:
        f=f*n
        return fact(n-1,f)
n=int(input('Enter the number to find factorial:'))
f=1
res=fact(n,f)
print(res)
