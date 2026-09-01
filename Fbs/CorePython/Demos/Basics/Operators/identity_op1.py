#it will not check the value it will check memory location is same or not
#int are immutable-can be reuse

#1. in
x = 10
y = 10 #reuse as int is immutable
z = 20
li1 = [10 , 20]
li2 = [10 , 20]

print(x is y)
print(x is z)

print(li1 is li2) #it gives flase as li1 and li2 are same value but the memory location is different as list are mutable(can't be reuse)

