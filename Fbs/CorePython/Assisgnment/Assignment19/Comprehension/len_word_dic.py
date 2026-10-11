# Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user)

s=input("Enter the string:")
s.split()
d1={i:len(i) for i in s.split()}
print(d1)