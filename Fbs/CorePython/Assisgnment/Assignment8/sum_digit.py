#WAP to find sum of digits of number

def sumDigit(n):
    sum=0
    while(n>0):
        d=n%10
        sum=sum+d
        n=n//10
    return sum
num=int(input('Enter the number :'))
res=sumDigit(num)
print(f'The sum of digit of number {num} is {res}')

