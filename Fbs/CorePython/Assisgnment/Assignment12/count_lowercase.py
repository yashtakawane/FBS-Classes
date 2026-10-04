def countLowercase(s1):
    count = 0

    for i in s1:
        if i >= 'a' and i <= 'z':
            count += 1

    return count


s1 = input('Enter the string: ')

res = countLowercase(s1)

print(f'Number of lowercase characters: {res}')