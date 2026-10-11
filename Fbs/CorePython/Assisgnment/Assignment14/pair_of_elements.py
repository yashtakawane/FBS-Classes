def pairs(l1, target):
    s1 = set()

    for i in range(0, len(l1)):
        for j in range(i + 1, len(l1)):
            if l1[i] + l1[j] == target:
                s1.add((l1[i], l1[j]))

    return s1


l1 = [1, 2, 3, 4, 5, 6, 7]
target = 8

res = pairs(l1, target)
print(res)