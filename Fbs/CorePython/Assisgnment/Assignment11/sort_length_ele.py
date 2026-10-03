def sortLengthElement(l1):
    for i in range(1, len(l1)):
        for j in range(0, len(l1) - 1):

            n1 = l1[j]
            n2 = l1[j + 1]

            count1 = 0
            count2 = 0

            while n1 > 0:
                count1 += 1
                n1 = n1 // 10

            while n2 > 0:
                count2 += 1
                n2 = n2 // 10

            if count1 > count2:
                l1[j], l1[j + 1] = l1[j + 1], l1[j]

    return l1


l1 = [100, 22, 123, 2, 345, 2111]

res = sortLengthElement(l1)
print(res)