#Accept no. of passengers from user and per ticket cost. Then accept age of each
#passenger and then calculate total amount to ticket to travel for all of them based on
#following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

total_amount=0
passengers=int(input('Enter the total number of passengers:'))
ticket = float(input('Enter the ticket per person:'))
for i in range(1,passengers+1):
    age = int(input(f'Enter the age of person {i}:'))
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
    print(f'The Ticket of all the people is:{total_amount}')
