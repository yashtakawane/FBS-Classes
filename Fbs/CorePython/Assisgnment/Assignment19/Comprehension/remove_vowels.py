# Remove all of the vowels in a string (take input from user)
s = input("Enter the string: ")

l1 = [i for i in s if i.lower() not in "aeiou"]

s2 = "".join(l1)

print("The string without vowels is:", s2)