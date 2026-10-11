def wordFrequency(l1):
    s1 = set()

    for i in range(0, len(l1)):
        words = l1[i].split()
        for j in words:
            s1.add(j)

    for word in s1:
        count = 0
        for i in range(0, len(l1)):
            words = l1[i].split()
            for j in words:
                if word == j:
                    count += 1
        print(word, ":", count)


l1 = ["hello world", "hello python", "world python", "hello"]
wordFrequency(l1)