def intersection(l1,l2,l3):
    for i in range(0,len(l1)):
        for j in range(0,len(l2)):
            if l1[i]==l2[j]:
                l3.append(l1[i])
    return l3

l1=[10,20,30,40]
l2=[20,33,21,10,50]
l3=[]
res=intersection(l1,l2,l3)
print(res)