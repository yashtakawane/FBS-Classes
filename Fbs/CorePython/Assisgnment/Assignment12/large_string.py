def largerString(s1, s2):
    count1 = 0
    count2 = 0

    for i in s1:
        count1 += 1

    for i in s2:
        count2 += 1

    if count1 > count2:
        return s1
    else:
        return s2


s1 = input('Enter first string: ')
s2 = input('Enter second string: ')

res = largerString(s1, s2)

print(f'Larger string is: {res}')