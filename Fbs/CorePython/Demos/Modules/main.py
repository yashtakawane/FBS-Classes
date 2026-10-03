#direct import(type 1 )---we have imported demo1 module directly here

# import demo1 
# demo1.add(12,12)
# print(demo1.pname) #to acces member this is syntax  

#from modulename import member(type2)

# from demo1 import add
# add(12,5)

#from modulename import member's(type3)

# from demo1 import add,pname
# add(12,5)
# print(pname)

#from module name import all(*) (type4)

# from demo1 import *
# add(12,2)
# sub(12,2)
# print(pname)

#note:use (*) only when there are too many words,dont use always because it slow down application

#Alicename() (nickname) (type5)

import demo1 as d
d.add(12,2)
d.sub(12,2)
print(d.pname)