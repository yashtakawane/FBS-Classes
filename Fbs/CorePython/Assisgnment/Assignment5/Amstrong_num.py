#WAP to print Armstrong number within a given range
n=int(input('Enter the range:'))
for i in range(1,n+1):
    count=len(str(i))
    temp=i
    arno=0
    while(i>0):
        dig=i%10
        arno=arno+(dig**count)
        i//=10
    if(temp==arno):
        print(f'{temp} is a armstrong number')
