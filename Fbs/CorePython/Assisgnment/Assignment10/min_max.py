def minMax(l1):
    
    min_element=l1[0]
    max_element=l1[0]
    for i in range(0,len(l1)):
        if(l1[i]<min_element):
            min_element=l1[i]
            

    for i in range(0,len(l1)):
        if(l1[i]>max_element):
            max_element=l1[i]
    return (f'MAximum element is {max_element} at index {i}'
            f'Minimum element is {min_element} at index {i}')


l1=[10,20,55,60,99,50]
res=minMax(l1)
print(res)

 