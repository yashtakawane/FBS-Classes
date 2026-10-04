def addKeyValue(d1, n, value):
    d1[n] = value
    return d1


d1 = {1: "Yash", 2: "Raj"}

n = int(input('Enter the key to add: '))
value = input('Enter the value to add: ')

res = addKeyValue(d1, n, value)

print(res)