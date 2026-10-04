def removeKey(d1, n):

    if n in d1:
        d1.pop(n)

    return d1


d1 = {1: "Yash", 2: "Raj", 3: "Amit"}

n = int(input('Enter the key to remove: '))

res = removeKey(d1, n)

print(res)