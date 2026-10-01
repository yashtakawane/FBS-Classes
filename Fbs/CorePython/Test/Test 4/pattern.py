n = 21  

for i in range(n):
    
    if i == 0 or i == n - 1:
        for j in range(n):
            print('*', end='')
   
    else:
        spaces = n - 1 - i
        for j in range(spaces):
            print(' ', end='')
        print('*', end='')
    print() 