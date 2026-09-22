def duplicateRemove(l1, l2):

    for i in range(0, len(l1)):

        found = False

        for j in range(0, len(l2)):
            if l1[i] == l2[j]:
                found = True
                break

        if found == False:
            l2.append(l1[i])

    return l2


l1 = [10, 20, 30, 20, 30, 40, 50]
l2 = []
res = duplicateRemove(l1, l2)
print(res)