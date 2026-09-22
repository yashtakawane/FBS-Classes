def newCubelist(l1,l2):
    for i in range(0,len(l1)):
        l2.append(l1[i]**3)
    return l2

l1=[10,20,30]
l2=[]
res=newCubelist(l1,l2)
print(res)