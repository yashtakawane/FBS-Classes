def sumItems(d1):
    sum=0
    for keys in d1:
        items=d1.get(keys)
        sum=sum+items
    return sum

d1 = {1: 10, 2: 20, 3: 30}
res=sumItems(d1)
print(res)