def longestPrefix(l1):
    s1 = set()
    prefix = ""

    for i in range(0, len(l1[0])):
        s1.clear()

        for j in range(0, len(l1)):
            if i < len(l1[j]):
                s1.add(l1[j][i])

        if len(s1) == 1:
            prefix += l1[0][i]
        else:
            break

    return prefix


l1 = ["flower", "flow", "flight"]
res = longestPrefix(l1)
print(res)