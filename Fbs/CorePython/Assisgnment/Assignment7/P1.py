for i in range(1,6):
    for j in range(1,6-i):
        print('_',end=' ')

    if(i+j==6):
        print('*',end=' ')

    print()   