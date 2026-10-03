# #1. Direct import
# import mypack.abc
# import mypack.xyz
# mypack.abc.greet1()
# a=mypack.abc.iname
# print(a)
# mypack.xyz.greet()

#2. From packagename.modulename import member
# from mypack.abc import greet1
# greet1()

# #3. from packagename.modulename import members
# from mypack.abc import greet1,iname
# from mypack.xyz import greet
# greet1()
# print(iname)
# greet()


#4.from packagename.modilename import (*)

# from mypack.xyz import greet
# from mypack.abc import *

# greet()
# greet1()
# print(iname)

#5. Alicename
# import mypack.abc as b
# import mypack.xyz as a
# print(b.iname)
# a.greet()
# b.greet1()