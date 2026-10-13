# 1. Develop a simple calculator program that performs basic arithmetic operations (+,
# -, *, /) on two numbers provided by the user. The program should ask the user for
# the numbers and the operator. However, the program should handle the following
# exceptions:
# a. Invalid Number: If the user enters a number that is not valid, catch the
# exception and display an error message.
# b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
# "/", catch the exception and display an error message.
# c. Division by Zero: If the user tries to divide by zero, catch the exception and
# display an error message.
# Write a program that performs the requested arithmetic operation and
# handles the exceptions as described above.


try:

    a=int(input('Enter the number1:'))
    b=int(input('Enter the number2:'))
    o=input('Enter the operator:')

    if o=='+':
        print("Result add:",a+b)
    elif o=='-':
        print('Result sub:',a-b)
    elif o == '*':
        print('Result multiply:',a*b)
    elif o=='/':
        print('Result div:',a/b)
    else:
        raise ValueError("Enter Valid Operator")

except ValueError as v:
    print(v)
except ZeroDivisionError:
    print('ERROR:Cannot be divide by Zero')
except Exception as e:
    print(e) 