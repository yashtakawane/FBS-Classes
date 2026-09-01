#Write a program to accept an integer amount from user and tell minimumnumber of notes needed for representing that amount.

amount = int(input('Enter the amount of rupees:'))
temp = amount
note500 = amount // 500
amount = amount % 500

note200 = amount // 200
amount = amount % 200


notee100 = amount // 100
amount = amount % 100


notee50 = amount // 50
amount = amount % 50


notee20 = amount // 20
amount = amount % 20


notee10 = amount // 10
amount = amount % 10


notee5 = amount // 5
amount = amount % 5


notee2 = amount // 2
amount = amount % 2


notee1 = amount // 1
amount = amount % 1

print(f'''The given rupess {temp} in notes is:
notes of 500 are:{note500}
notes of 200 are:{note200}
notes of 100 are:{notee100}
notes of 50 are:{notee50} 
notes of 20 are:{notee20} 
notes of 10 are:{notee10} 
notes of 5 are:{notee5} 
notes of 2 are:{notee2} 
notes of 1 are:{notee1}''')
