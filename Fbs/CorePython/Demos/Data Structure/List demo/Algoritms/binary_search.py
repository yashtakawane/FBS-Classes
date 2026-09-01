def binarySearch(li,searchEle):
    beg=0
    end=len(li)-1
    while(beg<=end):
        #print('beg',beg)
        #print('end',end)
    
        mid=(beg+end)//2
        #print('mid',mid)
        #print('search_ele',searchEle)
        #print('mid ele',li[mid])

        if(searchEle==li[mid]):
            #print('match condition')
            return mid
        elif(searchEle<li[mid]):
            #print('les then')
            end=mid-1
        elif(searchEle>li[mid]):
            #print('greater then')
            beg=mid+1
    else:
        return -1

li=[10,20,30,40,50,60] #list should always sorted(in ascending order)
                       #and duplicate values are not allowed in list
ele=int(input('Enter the element to search:'))
res=binarySearch(li,ele)
#print(res)
if(res != -1):
    print(f'{ele} is present at index {res}')
else:
    print(f'{ele} is not present in list')

#for manual debugging we can print all the condition for better understanding