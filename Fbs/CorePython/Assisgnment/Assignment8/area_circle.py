#Write a program to calculate area of circle

def areaCircle(r):
    area=3.14*r**2
    return area

radius=float(input('Enter the radius of circle:'))
res=areaCircle(radius)
print(f'The area of circle is {res}')