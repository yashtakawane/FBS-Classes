#it is the same qus from assignment3 whos redundancy was too high so it is solve using looping
total_amount=0
no=int(input('Enter the total number of people to buy ticket:'))
i=1
while(i<=no):
    age=int(input(f'Enter the age of the {i} person:'))
    ticket=float(input('Enter the prize of ticket:'))
    if(age<12):
        discount=ticket*(30/100)
        print(f'Passenger gets discount of {discount}')
        total_amount=total_amount+(ticket-discount)
    elif(age>59):
        discount=ticket*(50/100)
        print(f'Passenger gets discount of {discount}')
        total_amount=total_amount+(ticket-discount)
    else:
        print('You have got no discount')
        total_amount=total_amount+ticket
    i+=1
print(f'The Ticket of all the people is:{total_amount}')
   


    
            