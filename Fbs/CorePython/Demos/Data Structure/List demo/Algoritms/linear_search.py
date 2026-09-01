def linearSearch(li, searchEle): #2 parameter list and element which has to check wheter present or not
    for ind in range(0,len(li)):
        if(searchEle == li[ind]): 
            return ind #if the elemnt is present loop will break using return and give index(ind)
    else:         #looping else is used as the for loop executes without return ind else will execute
        return -1  #it is used because if element is there positive index will return

li=[10,33,56,67,35,35]
ele=int(input('Enter the element to search:'))
res=linearSearch(li,ele)
#print(res)
if(res != -1):
    print(f'{ele} is present at index {res}')
else:
    print(f'{ele} is not present in list')