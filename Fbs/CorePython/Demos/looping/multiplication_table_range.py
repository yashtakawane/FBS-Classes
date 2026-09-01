n = int(input('Enter number:'))
#for val in range(n, n * 10 + 1,n): #table 
for val in range(n * 10, n - 1,-n): #reverse table backwards
    print(val)