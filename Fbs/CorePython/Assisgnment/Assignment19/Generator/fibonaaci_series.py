def fib(n):
    i=0
    
    a=-1
    b=1

    while(i<n):
        c=a+b
        yield c
        a=b
        b=c

        i+=1
n=int(input("enter the limit:"))

res=fib(n)
# for i in res:
#     print(i,end=' ')
print(next(res))
print(next(res))
print(next(res))
