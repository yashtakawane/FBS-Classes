area = float(input("Enter area of one wall: "))
interior_cost = float(input("Enter interior wall cost: "))
exterior_cost = float(input("Enter exterior wall cost: "))

interior = area * 4
exterior = area * 6

total_cost = (interior * interior_cost) + (exterior * exterior_cost)

print("Total painting cost =", total_cost)