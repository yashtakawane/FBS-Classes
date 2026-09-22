def searchElement(l1,search_ele):
    count=0
    for i in range(0,len(l1)):
        if(search_ele==l1[i]):
            count+=1

    return (f'The entered number: {search_ele} is present {count} times')

l1=[10,20,33,45,39,20]
search_ele=int(input('Enter the number to search'))
res=searchElement(l1,search_ele)
print(res)