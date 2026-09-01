#Program to Find the Roots of a Quadratic Equation

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d = b ** 2 - 4*a*c

root = (-b + (d) ** 0.5) / (2 * a) # **0.5 is used as square root

print(f'The root of quadratic equation is {root}')