#Write a program to calculate profit or loss.
selling_prize = float(input('Enter the selling prize:'))
actual_prize = float(input('Enter the actual prize:'))

if(actual_prize < selling_prize):
    print('It is selled at profit')
else:
    print('It is selled at loss')