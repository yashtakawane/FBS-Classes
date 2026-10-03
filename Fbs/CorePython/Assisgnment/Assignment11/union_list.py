def unionList(l1, l2, l3):

    for i in range(0, len(l1)):
        l3.append(l1[i])

    for i in range(0, len(l2)):
        found = False

        for j in range(0, len(l3)):
            if l2[i] == l3[j]:
                found = True
                break

        if found == False:
            l3.append(l2[i])

    return l3


l1 = [10, 20, 30, 40]
l2 = [30, 40, 50, 60]
l3 = []

res = unionList(l1, l2, l3)

print(res)