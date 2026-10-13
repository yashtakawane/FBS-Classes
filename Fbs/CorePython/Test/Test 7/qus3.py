# Write a Python program that generates a list of odd numbers from 1
# to 50 using list comprehension and filters out the even numbers

l1 = [i for i in range(1, 51) if i % 2 != 0]

print(l1)