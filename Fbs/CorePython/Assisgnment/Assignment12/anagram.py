# def anagram(s1,s2):
#     count=0
#     if len(s1)!=len(s2):
#         return "Strings are not anagram"

#     else:
#         for i in range(0,len(s1)):
#             for j in range(0,len(s2)):
#                 if s1[i]==s2[j]:
#                     count+=1

#     if count==len(s1):
#         return "Strings are anagram"
#     else:
#         return 'String is not anagram'

# s1=input('Enter the string1:')
# s2=input('Enter the string2:')
# res=anagram(s1,s2)
# print(res)

def anagram(s1, s2):

    if len(s1) != len(s2):
        return "Strings are not anagram"

    for i in range(0, len(s1)):

        count1 = 0
        count2 = 0

        for j in range(0, len(s1)):
            if s1[i] == s1[j]:
                count1 += 1

        for j in range(0, len(s2)):
            if s1[i] == s2[j]:
                count2 += 1

        if count1 != count2:
            return "Strings are not anagram"

    return "Strings are anagram"


s1 = "silent"
s2 = "listen"

res = anagram(s1, s2)

print(res)