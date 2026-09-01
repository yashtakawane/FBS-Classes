days1 = int(input('Enter days:'))

years = days1 // 365
days = days1 % 365

weeks = days // 7
days = days % 7 

print(f'{days1} is equal to {years},{weeks}, and {days}')