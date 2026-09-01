#Find the sum of three-digit number.

num = int(input('Enter three digit number:'))

#first find digits on the place of hundereds tens ones

hundereds = num // 100
tens = (num // 10) % 10
one = num % 10

sum = hundereds + tens + one

print(f'The sum of digits of three digit number is {sum}')