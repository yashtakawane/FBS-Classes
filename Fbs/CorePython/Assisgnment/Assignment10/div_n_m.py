def divisibleMN(l1,l2,m,n):
    for i in range(0,len(l1)):
        if(l1[i]%m==0 and l1[i]%n==0):
            l2.append(l1[i])
    return l2
m=int(input('Enter m:'))
n=int(input('Enter n:'))
l1=[10,20,33,44,5,43,42,50,60]
l2=[]
res=divisibleMN(l1,l2,m,n)
print(res)