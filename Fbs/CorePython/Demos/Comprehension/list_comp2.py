even_li=[ele for ele in range(1,11) if ele % 2==0]

print(even_li)  

#---------sqaure root
# li=[1,4,36,49,9]
# l2=[]

# for i in li:
#     new_element=i**0.5
#     l2.append(new_element)

# print(l2)

# li=[1,4,36,49,9]
# new_element=[i**0.5 for i in li]
# print(new_element)

#------odd number
# li=[10,2,3,4,7,11,33]
# new=[]

# for i in li:
#     if(i%2!=0):
#         new.append(i)

# print(new)

# li=[10,2,3,4,7,11,33]
# new=[ele for ele in li if (ele%2!=0)]
# print(new)

# li=[10,2,3,4,7,11,33]
# new=[]

# for i in li:
#     if(i%2!=0):
#         new.append(i+10)

# print(new)
# li=[10,2,3,4,7,11,33]
# new=[i+10 for i in li if (i%2!=0)]
# print(new)
#--------give even odd

# li=[10,2,3,4,7,11,33]
# new=[]

# for i in li:
#     if(i%2!=0):
#         new.append('Odd')
#     else:
#         new.append('Even')
# print(new)

li=[10,2,3,4,7,11,33]
new=['odd' if (ele%2!=0) else 'even' for ele in li]
print(new)

