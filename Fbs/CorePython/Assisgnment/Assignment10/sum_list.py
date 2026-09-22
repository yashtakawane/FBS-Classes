def sumList(li):

    sum = 0

    for ind in range(0, len(li)):
        sum = sum + li[ind]

    return sum


li = []

n = int(input('Enter the number of elements: '))

for i in range(0, n):
    num = int(input('Enter the element: '))
    li.append(num)

res = sumList(li)

print(f'The sum of all elements in list is {res}')