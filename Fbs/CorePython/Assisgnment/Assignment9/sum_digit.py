#Write a program to find sum of digits using recursion.
def sumDigit(n,sum):
    if n == 0:
        return sum
    else:
        d=n%10
        n=n//10
        sum=sum+d
        return sumDigit(n,sum)

n=int(input('Enter the number:'))
sum=0
res=sumDigit(n,sum)
print(res)