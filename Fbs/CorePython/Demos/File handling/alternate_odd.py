def alternateOdd(l1, l2):
    alternative = 0

    for i in range(0, len(l1)):
        if l1[i] % 2 != 0:
            if alternative % 2 == 0:
                l2.append(l1[i])
            alternative += 1

    return l2


l1 = [1, 3, 2, 21, 18, 12, 9]
l2 = []

res = alternateOdd(l1, l2)
print(res)