#WAP to print factorial of a number .
n=int(input('Enter the number to find factorial: '))
mul=1
i=1
while(i<=n):
    mul=mul*i
    i+=1
print(mul)