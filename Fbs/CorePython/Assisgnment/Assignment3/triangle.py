#Write a program to input angles of a triangle and check whether triangle is valid or not.
angle1 = int(input('Enter angle 1st:'))
angle2 = int(input('Enter angle 2nd:'))
angle3 = int(input('Enter angle 3nd:'))

sum = angle1 + angle2 + angle3

if(sum == 180):
    print("It is a triangle")
else:
    print('It is not a triangle')