#Sum of all prime numbers between 1 to n

def sumPrime(n):
    sum=0
    for i in range(1,n+1):
        count=0
        for j in range(1,n+1):
            if(i%j==0):
                count+=1
        if(count==2):
            sum=sum+i
    return sum

n=int(input('Enter n:'))
res=sumPrime(n)
print(f'The sum of all prime number till {n} is {res}')
