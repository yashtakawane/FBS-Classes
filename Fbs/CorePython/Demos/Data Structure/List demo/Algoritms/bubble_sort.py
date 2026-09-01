def bubbleSort(li):
    size=len(li)
    for i in range(1,size):#range is taken from 1 because to run inner loop size-1 times
        for j in range(0,size-i): #(size-0)==(6-0==6) this is wrong so range is taken from 1
            if(li[j]>li[j+1]):
                li[j],li[j+1] = li[j+1],li[j]
                #print(li) to check the process


li=[60,50,40,30,20,10]
print('Before sorting',li)
bubbleSort(li)
print('After sorting',li)