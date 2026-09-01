product1=int(input('Enter the prize of product 1:'))
product2=int(input('Enter the prize of product 2:'))
product3=int(input('Enter the prize of product 3:'))
product4=int(input('Enter the prize of product 4:'))
product5=int(input('Enter the prize of product 5:'))

total=(product1+product2+product3+product4+product5)

total_bill=total+(total*18/100)

print(f'The total bill including 18% GST is:{total_bill}')