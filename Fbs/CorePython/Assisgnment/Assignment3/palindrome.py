#Write a program to check if given 3 digit number is a palindrome or not.

num = int(input('Enter the 3 digit number:'))
temp = num
ones = num % 10
num = num // 10
tens = num % 10
num = num // 10
hundred = num % 10
num = num // 10
#print(f'{hundred} is h ,{tens} is t,{ones} is o')
if(hundred == ones):
    print("The number is palindrome")
else:
    print('The number is not a palindrome')