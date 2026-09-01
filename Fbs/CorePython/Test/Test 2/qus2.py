num = int(input('Enter three digit number:'))

ones=num%10
num=num//10

tens=num%10
num=num//10

hundres=num%10
num=num//10

if(hundres == 2*tens and hundres == ones/2):
    print('yes,you have done it')
else:
    print('please try next time')

#print(hundres,tens,ones)