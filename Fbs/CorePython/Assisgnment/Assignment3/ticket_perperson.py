#Accept age of five people and also per person ticket amount and then calculate totalamount to ticket to travel for all of them based on following condition :a. Children below 12 = 30% discountb. Senior citizen (above 59) = 50% discountc. Others need to pay full
total_amount=0
age1 = int(input('Enter the age of first person:'))
ticket1 = float(input('Enter the ticket of first person:'))

if(age1<12):
    discount=ticket1*(30/100)
    print(f'Passenger gets discount of {discount}')
    total_amount=total_amount+(ticket1-discount)
elif(age1>59):
    discount=ticket1*(50/100)
    print(f'Passenger gets discount of {discount}')
    total_amount=total_amount+(ticket1-discount)
else:
    print('You have got no discount')
    total_amount=total_amount+ticket1
print(f'The Ticket of all the people is:{total_amount}')

age2 = int(input('Enter the age of second person:'))
ticket2 = float(input('Enter the ticket of second person:'))

if(age2<12):
    discount=ticket2*(30/100)
    print(f'Passenger gets discount of {discount}')
    total_amount=total_amount+(ticket2-discount)
elif(age2>59):
    discount=ticket2*(50/100)
    print(f'Passenger gets discount of {discount}')
    total_amount=total_amount+(ticket2-discount)
else:
    print('You have got no discount')
    total_amount=total_amount+ticket2
print(f'The Ticket of all the people is:{total_amount}')

age3 = int(input('Enter the age of third person:'))
ticket3 = float(input('Enter the ticket of third person:'))

if(age3<12):
    discount=ticket3*(30/100)
    print(f'Passenger gets discount of {discount}')
    total_amount=total_amount+(ticket3-discount)
elif(age3>59):
    discount=ticket3*(50/100)
    print(f'Passenger gets discount of {discount}')
    total_amount=total_amount+(ticket3-discount)
else:
    print('You have got no discount')
    total_amount=total_amount+ticket3
print(f'The Ticket of all the people is:{total_amount}')

age4 = int(input('Enter the age of fourth person:'))
ticket4 = float(input('Enter the ticket of fourth person:'))

if(age4<12):
    discount=ticket4*(30/100)
    print(f'Passenger gets discount of {discount}')
    total_amount=total_amount+(ticket4-discount)
elif(age4>59):
    discount=ticket4*(50/100)
    print(f'Passenger gets discount of {discount}')
    total_amount=total_amount+(ticket4-discount)
else:
    print('You have got no discount')
    total_amount=total_amount+ticket4
print(f'The Ticket of all the people is:{total_amount}')

age5= int(input('Enter the age of fifth person:'))
ticket5 = float(input('Enter the ticket of fifth person:'))

if(age5<12):
    discount=ticket5*(30/100)
    print(f'Passenger gets discount of {discount}')
    total_amount=total_amount+(ticket5-discount)
elif(age5>59):
    discount=ticket5*(50/100)
    print(f'Passenger gets discount of {discount}')
    total_amount=total_amount+(ticket5-discount)
else:
    print('You have got no discount')
    total_amount=total_amount+ticket5
print(f'The Ticket of all the people is:{total_amount}')

#This code redudancy is too high so we can do this using looping which is done in looping folder

