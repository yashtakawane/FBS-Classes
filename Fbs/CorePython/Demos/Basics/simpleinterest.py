#take input
p = int(input('Enter principle:'))
r = float(input('Enter rate:'))
t = int(input('Enter time(year):'))

#perform operation
SI = (p * r * t) / 100

#display result
print(f'Simple Interest is {SI}')
