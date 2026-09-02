def fibonacci(a, b, n):

    if n == 0:
        return
    else:
        print(a, end=' ')
        c = a + b
        return fibonacci(b, c, n-1)


n = int(input('Enter the limit of series: '))

a = 0
b = 1

fibonacci(a, b, n)
    