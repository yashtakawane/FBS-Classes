#1.to make parameters optional default parameters are used
#2.parameter - default (Assigning value to parameter in function definition)
#3.if we passs value to default parameter,it takes passed value
    #if we dont pass value to default para,it takes default value
#4.flow is from right to left

def emp(id, name,sal,dept='Backoffice'):
    print('ID:',id)
    print('Name:',name)
    print('Salary:',sal)
    print('DEPARTMENT:',dept)

emp(11,'YASH',111111,'IT')
print('#########')
emp(112,'SAKSHI',12)