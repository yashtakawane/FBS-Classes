# Write a function to which we pass a parameter and
# print the factors of a given number
def factorial(a):
    for i in range(1,a+1):
        if a % i == 0:
            print(i,end=' ')
     
            
a = int(input('Enter the number to get factorials:'))
factorial(a)


    