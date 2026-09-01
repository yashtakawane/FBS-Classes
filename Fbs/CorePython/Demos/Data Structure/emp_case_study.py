def addEmp():
    id = int(input('Enter ID:'))
    nm=input('Enter Name:')
    dept=input('Enter the departnment:')
    sal=float(input('Enter the salary:'))
    if(id not in emp_details):
        emp_details[id]=[id,nm,dept,sal]
        return 'Employee added successfully.'
    else:
        return 'Employee ID is already available'
    
def updEmp():
    id=int(input('Enter ID:'))
    er=emp_details.get(id)
    if(er):
        nm=input(f'Enter new NAME({er[1]}):') or er[1]
        dept=input(f'Enter new DEPT({er[2]}):') or er[2]
        sal=float(input(f'Enter new SALARY({er[3]}):') or 0) or er[3]

        emp_details[id]= [id,nm,dept,sal]
        return 'Emplyee updates successfully'
    else:
        return 'Employee ID not found'
    
def deletEmp():
    
    id=int(input('Enter ID:'))
    if(id in emp_details):
        del emp_details[id]
        return 'Employee deleted successfully'
    else:
        return 'Employee ID not found'


def searchEmp():
    id=int(input('Enter ID:'))
    er=emp_details.get(id)
    if(er):
        print('ID:',er[0])
        print('Name:',er[1])
        print('Department:',er[2])
        print('Salary:',er[3])
    else:
        print('Employee ID not found')

def searchEmp():
    id=int(input('Enter the Employee ID to search:'))

    if id in emp_details:
        print(emp_details[id])
    else:
        print('Employee ID not present')
        
def showAllEmp():
    print(emp_details)


def empManage():
    ch=0
    while(ch!=6):
        print('#### EMPLOYEE MANAGNMENT ####')
        print('''Please select option from below:
        1. Add emp
        2. Update emp
        3. Delete emp
        4. Search emp
        5. Show all emp
        6. Logout''')
        ch=input('Enter your choice:')
        if(ch=='1'):
            res=addEmp()
            print(res)
        elif(ch=='2'):
            res=updEmp()
            print(res)
        elif(ch=='3'):
            res=deletEmp()
            print(res)
        elif(ch=='4'):
            res=searchEmp()
            print(res)
        elif(ch=='5'):
            showAllEmp()
        elif(ch=='6'):
            print('Logged Out..')

        
def login():
    print('##### LOGIN PAGE #####')
    uid='admin'
    passw='1234'
    username=input('Enter Username:')
    password=input('Enter password:')
    if(uid==username and passw==password):
        empManage()
    else:
        print('Invalid userID and Password..')

emp_details={}
ch=0
while(ch!='2'):
    print('''Please select option from below
    1.LogIn
    2.Exit''')
    ch=input('Enter choice:')
    if(ch=='1'):
        login()
    elif(ch=='2'):
        print('Thanks for visiting')
    else:
        print('Invalid Choice...')