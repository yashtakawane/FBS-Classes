# Count the number of spaces in a string (take input from

s=input("Enter the string:")

l1=[i for i in s if (i==" ")]
print(f'Number of spaces is:{len(l1)}')