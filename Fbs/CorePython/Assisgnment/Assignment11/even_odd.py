def evenOdd(l1,l2,l3):
    for i in range(0,len(l1)):
        if l1[i] % 2 == 0:
            l2.append(l1[i])
        else:
            l3.append(l1[i])
    return l2,l3

l1=[10,20,33,40,55,60,77,80,99,100]
l2=[]
l3=[]
res=evenOdd(l1,l2,l3)
print(res)