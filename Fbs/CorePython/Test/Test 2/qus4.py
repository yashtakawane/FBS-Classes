height=int(input('Enter the height of wall:'))
length=int(input('Enter the length of wall:'))
cost=int(input('Enter the cost of painting per sqr m:'))

area=height*length*4

total_cost=area*cost

print(f'The total cost to paint all 4 walls is {total_cost}')