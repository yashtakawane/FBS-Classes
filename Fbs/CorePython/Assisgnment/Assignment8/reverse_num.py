#WAP to reverse number

def reverse(n):
    rev=0
    while(n>0):
        d=n%10
        n=n//10
        rev=rev*10+d
    return rev
num=int(input('Enter the number :'))
result=reverse(num)
print(f'The reverse of number {num} is {result}')
