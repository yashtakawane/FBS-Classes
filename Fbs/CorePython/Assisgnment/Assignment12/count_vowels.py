def countVowels(s1):
    count=0
    for i in range(0,len(s1)):
        if s1[i]=='a' or s1[i]=='e' or s1[i]=='i' or s1[i]=='o' or s1[i]=='u':
            count+=1
    return f'The number of vowels  is {count}'

s1=input('Enter the string 1:')
res=countVowels(s1)
print(res)