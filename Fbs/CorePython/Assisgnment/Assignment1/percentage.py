#Write a program to calculate the percentage of student based on marks of any 5 subjects
num1 = int(input('Enter marks for English:'))
num2 = int(input('Enter marks for Maths:'))
num3 = int(input('Enter marks for Science:'))
num4 = int(input('Enter marks for Marathi:'))
num5 = int(input('Enter marks for Social Studies:'))
num6 = int(input('Enter total marks of all subject:'))

sum = num1 + num2 + num3 + num4 + num5

percentage = (sum / num6) * 100

print(f'The percentage of student in 5 Subject is {percentage}')

