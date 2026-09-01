num1 = int(input('Enter starting number:'))
num2 = int(input('Enter ending number:'))

for val in range(num1,num2+1):
    if (val%2!=0):
        print(val)