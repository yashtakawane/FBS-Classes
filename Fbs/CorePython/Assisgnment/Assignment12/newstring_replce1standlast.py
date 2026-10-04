def replaceFirstwithLast(s1, s2):

    for i in range(0, len(s1)):
        if i == 0:
            s2 = s2 + s1[len(s1) - 1]
        elif i == len(s1) - 1:
            s2 = s2 + s1[0]
        else:
            s2 = s2 + s1[i]

    return s2


s1 = input('Enter the string: ')
s2 = ''

res = replaceFirstwithLast(s1, s2)

print(res)