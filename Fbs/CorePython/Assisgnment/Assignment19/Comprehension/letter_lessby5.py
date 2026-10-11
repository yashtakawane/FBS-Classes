# Find all of the words in a string that are less than 5 letters (take
# input from user)

s=input("Enter the string:")
s.split()
l1=[i for i in s.split() if (len(i) < 5)]
print("Words less then 5 letters are",l1)