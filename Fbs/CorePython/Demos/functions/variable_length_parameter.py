#1 to pass multiple values to function
#2. mention 1 asterrisk symbol (*) before parameter name in function definitiom
#3. Passed values are stored in tuple format
#4. use for loop to iterate values from tuple

def add(*data):
    sum=0
    for var in data:
        sum += var
    return sum

res=add(10,30,40,20,10,30,1,4,6,55)
print(res)