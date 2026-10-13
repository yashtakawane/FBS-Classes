# Write a Python program that takes a list of strings as input and
# returns a new list containing the uppercase versions of the strings
#  using list comprehension.

l1 = input("Enter strings separated by spaces: ")
l1.split()

l2 = [i.upper() for i in l1]

print("Uppercase strings:", l2)