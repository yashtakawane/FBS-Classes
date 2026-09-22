def reverse(l1,l2):
    for i in range(len(l1)-1,-1,-1):
        l2.append(l1[i])
    return l2

l1=[10,20,30,40]
l2=[]
res=reverse(l1,l2)
print(res)

