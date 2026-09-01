def selectionSor(li):
    size=len(li)
    for i in range(0,size-1):
        min_ele=i
        for j in range(i+1,size):
            if(li[j]<li[min_ele]):
                min_ele=j
        li[i],li[min_ele]=li[min_ele],li[i]


li=[60,50,40,30,20,10]
print('Before sorting',li)
selectionSor(li)
print('After sorting',li)