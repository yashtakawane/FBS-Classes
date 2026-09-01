# WAP to check whether entered number is Armstrong number or not

def armstrong(n):
    temp = n
    digits = len(str(n))
    sum = 0

    while n > 0:
        d = n % 10
        sum = sum + d ** digits
        n = n // 10

    if temp == sum:
        return True
    else:
        return False


n = int(input('Enter the number:'))

result = armstrong(n)

if result:
    print(f'{n} is an Armstrong number')
else:
    print(f'{n} is not an Armstrong number')