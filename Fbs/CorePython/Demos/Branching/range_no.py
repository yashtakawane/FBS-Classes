num = int(input('Enter the number:'))

if(num <= 0 and num > 0):
    if(num < 0):
        print(f'{num} is less then zero')
    else:
        print(f'{num} is zero')
elif(num <= 50):
    print(f'{num} is between 0 to 50')
elif(num <= 100):
    print(f'{num} is between 50 to 100')
elif(num <= 150):
    print(f'{num} is between 100 to 150')
elif(num <= 200):
    print(f'{num} is between 150 to 200')
elif(num <= 250):
    print(f'{num} is between 200 to 250')
else:
    print(f'{num} is grater then 250')