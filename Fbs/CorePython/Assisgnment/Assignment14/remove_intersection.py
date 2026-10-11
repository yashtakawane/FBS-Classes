def removeIntersection(s1, s2):
    s1.difference_update(s2)
    return s1

s1 = {10, 20, 30, 40, 50}
s2 = {15, 25, 30, 35, 40}

res = removeIntersection(s1, s2)
print(res)