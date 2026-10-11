def palindrome():
    n = 1
    while True:
        num = n
        rev = 0

        while num > 0:
            digit = num % 10
            rev = rev * 10 + digit
            num = num // 10

        if n == rev:
            yield n

        n += 1


res = palindrome()

for i in range(15):
    print(next(res), end=" ")