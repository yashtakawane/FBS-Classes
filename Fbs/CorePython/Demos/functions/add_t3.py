#without passing parameters
#with return value

def addition():
    num1=int(input('Enter number 1:'))
    num2=int(input('Enter number 2:'))

    add = num1+num2

    return add

result=addition()

print(f'The addition is {result}')

