#WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.
basic = float(input('Enter the salary:'))
da = basic * 0.1
ta = basic * 0.12
hra = basic * 0.15
finalsal = basic + da + ta + hra

print(f'Final salary is  {finalsal}')