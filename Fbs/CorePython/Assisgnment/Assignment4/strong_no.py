#WAP to check if given number Strong Number.
num=int(input('Enter the number to check strong number:'))
temp=num
sum=0
while(num>0):
    d=num%10
    num=num//10

    mult=1
    i=1

    while(i<=d):
        mult=mult*i
        i+=1
    sum=sum+mult
if(sum==temp):
    print(f'{temp} is a strong number ')
else:
    print(f'{temp} is not strong number ')