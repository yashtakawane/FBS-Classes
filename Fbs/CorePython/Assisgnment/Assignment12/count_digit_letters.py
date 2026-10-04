def countDigitsLetters(s1):
    digit_count = 0
    letter_count = 0

    for i in s1:
        if i >= '0' and i <= '9':
            digit_count += 1
        elif (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            letter_count += 1

    return digit_count, letter_count


s1 = input('Enter the string: ')

res = countDigitsLetters(s1)

print(f'Number of digits: {res[0]}')
print(f'Number of letters: {res[1]}')