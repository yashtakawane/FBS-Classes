def multiplyItems(d1):
    multiply=1
    for keys in d1:
        items=d1.get(keys)
        multiply=multiply*items
    return multiply

d1 = {1: 10, 2: 20, 3: 30}
res=multiplyItems(d1)
print(res)