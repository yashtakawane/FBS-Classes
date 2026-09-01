#WAP to print all integers upto n that aren’t divisible by 2 and 3.
n=int(input('Enter the number to check until the divisiblity: '))
for i in range(1,n+1):
    if(i%2==0):
        continue
    elif(i%3==0):
        continue
    else:
        print(i)