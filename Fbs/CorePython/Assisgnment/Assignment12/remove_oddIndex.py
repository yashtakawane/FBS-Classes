def removeOddIndex(s1):
    s2 = ""

    for i in range(0, len(s1)):
        if i % 2 == 0:
            s2 = s2 + s1[i]

    return s2


s1 = input('Enter the string: ')

res = removeOddIndex(s1)

print(res)