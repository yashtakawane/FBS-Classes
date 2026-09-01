#Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.

n=int(input('Enter the number of students:'))
average=0
for i in range(1,n+1):
    print(f'Marks for student {i}')
    num1 = int(input('Enter marks for English:'))
    num2 = int(input('Enter marks for Maths:'))
    num3 = int(input('Enter marks for Science:'))
    num4 = int(input('Enter marks for Marathi:'))
    num5 = int(input('Enter marks for Social Studies:'))
    num6 = int(input('Enter total marks of all subject:'))

    sum = num1 + num2 + num3 + num4 + num5

    percentage = (sum / num6) * 100

    print(f'The percentage of student in 5 Subject is {percentage}')

    average=average+percentage


print(f'The average percentage of all students are {average/n}') 

