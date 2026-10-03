#1. For memory optimization
#2. Generating values according to user requirment
#3. Use yeild keyword
#4. Maintain state(maintain stack frame) of function
#5. Iterate upcoming value using next from iterable

def generatevalues(n):

    for i in range(1,n+1):
        yield i
res=generatevalues(5)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
# print(next(res)) after the limit is over it will give erroe  as here it printed 5 times 
