def missingNumbers(s1, s2):
    missingInSecond = s1.difference(s2)
    missingInFirst = s2.difference(s1)

    return missingInSecond, missingInFirst


s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

res = missingNumbers(s1, s2)
print("Missing in second set:", res[0])
print("Missing in first set:", res[1])