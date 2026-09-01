#1. pass = to neglect expected indented blpck error
for i in range(1,10):
    pass

#2. break = to stop the loop
for i in range(1.10):
    if(i == 3):
        break  #loop will stop at i == 3 and will not execcute furture
    print(i)

#3.continue= to stop current iterarion
for i in range(1.10):
    if(i == 3):
        continue #loop will skip at i == 3 and will execcute furture
    print(i)

#4.else = Will execute when loop executed successfully
#a)
for i in range(1.10):
    if(i == 3):
        break  
    print(i)
else:
    print('Else is executed') #else will not execute because loopnis break
#b)
for i in range(1.10):
    if(i == 3):
        continue 
    print(i)
else:
    print('Else is executed')#else will execute as loop is completed