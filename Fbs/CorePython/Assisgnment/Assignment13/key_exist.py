def keyExistorNot(d1, n):

    if n in d1:
        return "Key Exists in Dictionary"
    else:
        return "Key doesn't Exist in Dictionary"


d1 = {1: "Yash", 2: "Raj"}

n = int(input('Enter the Key to check Existence: '))

res = keyExistorNot(d1, n)

print(res)