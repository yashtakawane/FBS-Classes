def infinite():
    i=1
    while(True):
        yield i
        i+=1

res=infinite()
print(next(res)) #there will be no limit abt printing as we have use while loop(infinite loop)
