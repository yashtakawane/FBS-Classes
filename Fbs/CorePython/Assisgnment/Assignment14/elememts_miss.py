def elements(s1,s2,s3):
    s3=s1.difference(s2)
    return s3

s1={10,20,30,40,50}
s2={11,23,20,40,30}
s3={}
res=elements(s1,s2,s3)
print(res)