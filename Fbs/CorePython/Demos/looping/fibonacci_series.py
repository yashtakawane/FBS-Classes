n = int(input('Enter the number of series:'))
a= -1
b = 1
for i in range(1 , n +1):
    c = a + b
    print(c , end = ' ')   #this is used to print in a single line instead of into multiple line
    a=b
    b=c