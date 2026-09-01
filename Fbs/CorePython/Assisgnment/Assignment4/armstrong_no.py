num=int(input('Enter the number:'))
count=len(str(num))
temp=num
arno=0
while(num>0):
    dig=num%10
    arno=arno+(dig**count)
    num//=10
if(temp==arno):
    print(f'{temp} is a armstrong number')
else:
    print(f'{temp} is not a armstrong number')