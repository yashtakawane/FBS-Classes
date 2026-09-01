#WAP to calculate selling price of book based on cost price and discount.
cost = float(input('Enter the actual cost of book:'))
discount = float(input('Enter the discount on book(in percentage):'))

discount_amount = (cost * discount) / 100
selling_price = cost - discount_amount


print(f'The selling price of book is {selling_price}')

