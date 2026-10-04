def dictonary(d1,n):
    for keys in range(1,n+1):
        d1[keys]=keys*keys

    return d1

d1={}
n=int(input('Enter the number of keys:'))
res=dictonary(d1,n)
print(res)