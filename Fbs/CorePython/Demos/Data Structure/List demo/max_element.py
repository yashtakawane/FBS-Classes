li=[10,40,30,220,40,304,22]

max=li[0]

for ind in range(1,len(li)):
    if(li[ind] > max):
        max=li[ind]

print('Maximun element:',max)

#WAP to calculate second max element from list