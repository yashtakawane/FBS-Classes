def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print("Returning cached result")
            return cache[args]

        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@memoize
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
print(factorial(5))