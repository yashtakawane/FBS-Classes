def wordCount(s1):
    words = s1.split()
    visited = []

    for i in range(0, len(words)):
        if words[i] not in visited:
            count = 0

            for j in range(0, len(words)):
                if words[i] == words[j]:
                    count += 1

            print(words[i], ":", count)
            visited.append(words[i])


s1 = input('Enter the string: ')

wordCount(s1)