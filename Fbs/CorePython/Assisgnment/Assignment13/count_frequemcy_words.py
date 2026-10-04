def wordFrequency(s1):
    d1 = {}
    words = s1.split()

    for word in words:
        if word in d1:
            d1[word] = d1[word] + 1
        else:
            d1[word] = 1

    return d1


s1 = input('Enter the string: ')

res = wordFrequency(s1)

print(res)