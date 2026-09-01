#WAP to print all numbers in a range divisible by a given number.
n = int(input('Enter the range: '))
num = int(input('Enter the number to check divisiblity: '))
for i in range(1,n+1):
    if(i%num==0):
        print(f'Number{i} is divisible by {num}')