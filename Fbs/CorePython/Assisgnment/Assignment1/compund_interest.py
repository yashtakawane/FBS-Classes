#Write a program to enter P, T, R and calculate Compound Interest.

p = int(input('Enter principle:'))
r = int(input('Enter rate:'))
t = int(input('Enter time(year):'))
n = int(input('Enter number of componding preiod per year:'))

CI = p * ((1 + r / 100 * n)) ** (n * t) - p

print(f'The compound interest is {CI}')