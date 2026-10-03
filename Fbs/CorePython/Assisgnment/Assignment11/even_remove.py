def evenRemove(l1):
    for i in range(len(l1) - 1, -1, -1):
        if l1[i] % 2 == 0:
            l1.pop(i)

    return l1


l1 = [10, 11, 20, 23, 30, 35, 60, 67, 70, 73]

res = evenRemove(l1)

print(res)