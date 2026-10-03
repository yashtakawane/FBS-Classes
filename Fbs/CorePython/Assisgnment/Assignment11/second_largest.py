def secondLargest(l1):
    for i in range(1,len(l1)):
        for j in range(0,len(l1)-1):
            if l1[j]>l1[j+1]:
                l1[j],l1[j+1]=l1[j+1],l1[j]
    return l1[len(l1)-2]

l1=[10,23,45,32,67]
res=secondLargest(l1)
print(f'The second largest is {res}')