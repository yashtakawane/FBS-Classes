def secondLargest(l1):
    max_element=l1[0]
    sec_Largest=l1[0]
    for i in range(0,len(l1)):
        if(l1[i]>max_element):
            sec_Largest=max_element
            max_element=l1[i]

        elif(l1[i]>sec_Largest):
            sec_Largest=l1[i]
    return sec_Largest

l1=[10,20,69,55,99]
res=secondLargest(l1)
print(res)