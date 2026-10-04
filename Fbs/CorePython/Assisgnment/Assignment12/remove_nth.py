def removeCharacter(s1, n):
    s2 = ""

    for i in range(0, len(s1)):
        if i != n:
            s2 = s2 + s1[i]

    return s2


s1 = input("Enter the string: ")
n = int(input("Enter the index to remove: "))

res = removeCharacter(s1, n)

print(res)