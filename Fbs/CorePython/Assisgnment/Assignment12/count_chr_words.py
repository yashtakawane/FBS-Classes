def countWordsCharacters(s1):
    char_count = 0
    word_count = 1

    for i in s1:
        char_count += 1

        if i == ' ':
            word_count += 1

    return word_count, char_count


s1 = input('Enter the string: ')

res = countWordsCharacters(s1)

print(f'Number of words: {res[0]}')
print(f'Number of characters: {res[1]}')