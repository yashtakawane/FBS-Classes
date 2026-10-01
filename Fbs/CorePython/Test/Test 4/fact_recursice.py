# Write a program to find factorial of given number using recursion

def fact(a):
    
    if a==0 or a==1:
        return 1
    else:
        return a * fact(a-1)
a = int(input('Enter the number to get factorials:'))
res=fact(a)
print(res)

