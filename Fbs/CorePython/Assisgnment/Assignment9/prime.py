#Write a program to check whether a number is prime or not using recursion.
def prime(n,j,count):
    if n+1==j:
        return count 
    else:
        
        if n%j==0:
            count+=1
        return prime(n,j+1,count)
n=int(input('Enter the number to check prime or not: '))
j=1
count=0
res=prime(n,j,count)
if(res==2):
    print('Number is prime:')
else:
    print('Number is not prime')

