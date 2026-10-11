def uniqueCombinations(l1, target):
    s1 = set()

    for i in range(0, len(l1)):
        for j in range(i + 1, len(l1)):
            for k in range(j + 1, len(l1)):
                if l1[i] + l1[j] + l1[k] == target:
                    s1.add(tuple(sorted((l1[i], l1[j], l1[k]))))

    return s1


l1 = [1, 2, 3, 4, 5, 6]
target = 9

res = uniqueCombinations(l1, target)
print(res)