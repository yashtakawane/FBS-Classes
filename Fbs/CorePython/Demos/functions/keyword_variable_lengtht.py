#1. to pass multiple values with meaning to function
#2.Mention 2 astersik value(**) before parameter name in function definition
#3. passed data stored in dictonary format
#4.use for loop on dict.items()to get values and keys

def emp(**data):
    for key , var in data.items():
        print(key, ':',var)

emp(id=101,age=33,add='Shirur',sal=1010000,dept='Admin')