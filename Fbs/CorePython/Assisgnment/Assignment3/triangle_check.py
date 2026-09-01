#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
side1 = float(input('Enter the 1st side:'))
side2 = float(input('Enter the 2nd side:'))
side3 = float(input('Enter the 3rd side:'))

if(side1 == side2 == side3):
    print('The triangle is equilateral')
elif((side1 == side2 != side3)or(side1 == side3 != side2)or(side2 == side3 != side1)):
    print('The triangle is isoceles')
else:
    print('The triangle is scalene')