#Write a program to check if given number is Armstrong or not using recursive
#function.
def amg(n, count):
    if n == 0:
        return 0
    else:
        d = n % 10
        n = n // 10
        return d**count + amg(n, count)


n = int(input('Enter the number to check:'))
count = len(str(n))

res = amg(n, count)

if n == res:
    print('Number is Armstrong')
else:
    print('Number is not Armstrong')