def sortSecondElement(l1):

    for i in range(1, len(l1)):
        for j in range(0, len(l1) - 1):

            if l1[j][1] > l1[j + 1][1]:
                l1[j], l1[j + 1] = l1[j + 1], l1[j]

    return l1


l1 = [[1, 5], [2, 3], [4, 8], [6, 1]]

res = sortSecondElement(l1)

print(res)