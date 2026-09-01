for i in range(1, 6):

    # spaces before numbers
    for j in range(1, 6-i):
        print(' ', end=' ')

    # first number
    print('1', end=' ')

    # middle/right part
    if i == 1:
        print()
    elif i == 5:
        for j in range(2, 6):
            print(f'{j} ', end=' ')
        print()
    else:
        for j in range(1, i):
            print('  ', end=' ')

        print(i)