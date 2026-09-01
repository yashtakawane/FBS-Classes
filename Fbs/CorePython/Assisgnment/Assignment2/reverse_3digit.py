#Write a program to reverse three-digit number.

num = int(input('Enter the three digit number to reverse:'))
b=num

ones = num % 10
num = num // 10

tens = num % 10
num = num // 10

hundreds = num % 10
num = num // 10

temp = ones
ones = hundreds
hundreds = temp

print(f'The reverse of number {b} is {hundreds}{tens}{ones}')
