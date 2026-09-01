#8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
num = int(input('Enter the last number of range: '))
for i in range(1,num+1):
    if(i%7==0 and i%5==0):
        print(f'Number {i} is divisible by 7 and multiple by 5')
    
    