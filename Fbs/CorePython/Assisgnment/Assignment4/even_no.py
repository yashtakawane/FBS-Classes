#WAP to print all even numbers until n.
n = int(input('Enter the number to print all even numbers until n:'))
i = 0
while(i<=n):
    if(i%2 == 0):
        print(i)
    i+=1