#Write a program to calculate area of rectangle
def areaRectangle(l,b):
    area=l*b
    return area
lenght=int(input('Enter the lenght of rectangle:'))
breadth=int(input('Enter the breadth of rectangle:'))
res=areaRectangle(lenght,breadth)
print(f'The area of rectangle is {res}')