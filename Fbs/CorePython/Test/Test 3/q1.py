# Write a program to print first n prime numbers
n = int(input("Enter how many prime numbers: "))
count=0
num=2

while count<n:
    prime=True
    for i in range(2,num):
        if num%i==0:
            prime=False
            
    if prime:
        print(num)
        count+=1
    num+=1

