def stringLength(s1):
    count = 0

    for i in s1:
        count += 1

    return count


s1 = input('Enter the string: ')

res = stringLength(s1)

print(f'Length of string is {res}')