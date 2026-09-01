#with passing parameters
##with return value


def addition(num1,num2):

    add = num1+num2

    return add
x=int(input('Enter no 1:'))
y=int(input('Enter no 2:'))

result=addition(x,y)

print(f'Addition is {result}')