def mergeSort(l1,l2):
    for i in range(0,len(l2)):
        l1.append(l2[i])
    for i in range(1,len(l1)):
        for j in range(0,len(l1)-1):
            if l1[j]>l1[j+1]:
                l1[j],l1[j+1]=l1[j+1],l1[j]

    return l1

l1=[10,22,54,34,23]
l2=[98,34,22,65,43]
res=mergeSort(l1,l2)
print(res)      