num = 1

for i in range(0, 10):

    l1 = []

    for j in range(0, 10):
        l1.append(num)
        num += 1

    if i % 2 == 1:
        l1.reverse()

    for j in range(0, 10):
        print(l1[j], end=" ")

    print()