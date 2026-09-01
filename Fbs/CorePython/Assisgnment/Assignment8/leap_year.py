# WAP to check whether entered year is leap year or not

def leapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input('Enter the year:'))

result = leapYear(year)

if result:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')