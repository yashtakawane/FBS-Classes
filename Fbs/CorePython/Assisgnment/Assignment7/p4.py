for i in range(1, 6):

    # spaces
    for j in range(1, 6-i):
        print(' ', end=' ')

    # increasing numbers
    for j in range(i, 2*i):
        print(j, end=' ')

    # decreasing numbers
    for j in range(2*i-2, i-1, -1):
        print(j, end=' ')

    print()