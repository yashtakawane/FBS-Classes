#Write a program to solve the following series :
#a. 1! + 2! + 3! + 4! + .....n!
print('This is ans of A):')
n = int(input('Enter the value of n: '))

fact = 1
sum = 0

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + fact

print('Sum of series =', sum)


#b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

print('This is a ans of B):')
n=int(input('Enter n :'))
sum=0
for i in range(1, n+1):
    sum=sum+ n**i

print('Sum of series ',sum)



#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
print('This is the ans of c)')
n = int(input('Enter the number of terms: '))

sum = 0
term = 1

for i in range(1, n + 1):
    sum = sum + term
    term = term * 2

print('Sum of geometric series =', sum)


#d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

print('This is the ans of d)')

a = int(input('Enter the value of a: '))

sum = 0

for i in range(1, 11):
    sum = sum + (a ** i) / i

print('Sum of series =', sum)

#e. x - x2/3 + x3/5 - x4/7 + .... to n terms
print('This is ans of e):')
x = int(input('Enter the value of x: '))
n = int(input('Enter the number of terms: '))

sum = 0
den = 1

for i in range(1, n + 1):

    term = (x ** i) / den

    if i % 2 == 0:
        sum = sum - term
    else:
        sum = sum + term

    den = den + 2

print('Sum of series =', sum)

