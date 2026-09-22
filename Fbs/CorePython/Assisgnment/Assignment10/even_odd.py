def evenOdd(l1,l2,l3):
    for i in range(0,len(l1)):
        if(l1[i]%2==0):
            l2.append(l1[i])
        else:
            l3.append(l1[i])
    return (f'''Even Element is {l2}
Odd Element list is {l3}''')

l1=[10,27,30,43,50,69,70,87,90]
l2=[]
l3=[]
res=evenOdd(l1,l2,l3)
print(res)