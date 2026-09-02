#Write a program to reverse a given number using recursive function.

def reverse(n,res):
    if n==0:
        return res
    else:
        d=n%10
        n=n//10
        res=res*10+d
        return reverse(n,res)

n=int(input('Enter the number to reverse:'))
res=0
rev=reverse(n,res)
print(rev)
