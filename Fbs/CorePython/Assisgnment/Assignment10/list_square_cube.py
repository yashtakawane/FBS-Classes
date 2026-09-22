def createList(l1,l2,l3):
    for i in range(0,len(l1)):
        l2.append(l1[i]**2)
        l3.append(l1[i]**3)

    return(f'''List is:{l1}
Square of elements in List:{l2}
Cube of elements in List:{l3} ''')
no_elements=int(input('Enter the number of elements in list:'))
l1=[]
for i in range(0,no_elements):
    i=int(input('Enter the number:'))
    l1.append(i)
l2=[]
l3=[]
res=createList(l1,l2,l3)
print(res)
