#Input 5 subject marks from user and display grade(eg.First class,Second class ..)
subject1 = int(input('Enter the marks of first subject/100:'))
subject2 = int(input('Enter the marks of second subject/100:'))
subject3 = int(input('Enter the mark of third subject/100:'))
subject4 = int(input('Enter the marks of fourth subject/100:'))
subject5 = int(input('Enter the marks of fiveth subject/100:'))

sum = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (sum/500)*100


if(percentage >= 75):
    print(f'The student has scored First class with {percentage} percentage')
elif(percentage >= 50):
    print(f'The student has scored Second class {percentage} percentage')
else:
    print(f'Student is Passed {percentage} percentage')