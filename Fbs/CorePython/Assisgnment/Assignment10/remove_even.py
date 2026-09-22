def removeEven(l1):

    for i in l1[:]:

        if i % 2 == 0:
            l1.remove(i)

    return l1


l1 = [10, 22, 33, 23, 44, 56, 67]

res = removeEven(l1)

print(res)