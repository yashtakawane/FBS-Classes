#employee          → Class
#e1, e2            → Objects
#__init__()        → Constructor
#self.id/name/sal  → Instance variables
#display()         → Method
class employee():
    def __init__(self,eid,ename,esal): #__init__ is the constructor which initialize with object automatically
        self.id=eid # self.id = state; stores employee ID for each object
        self.name=ename# self.name = state; stores employee name for each object
        self.sal=esal # self.sal = state; stores employee salary for each object


    def getName(self): #getter and setter are used to access or change state by behaviour as state is hidden in real
        return self.name
    def setName(self,newName):
        self.name=newName
    
        
    def getSal(self):
        return self.sal
    def setSal(self,newsal):
        self.sal=newsal
    
        
    def getId(self):
        return self.id
    def setId(self,newid):
        self.id=newid


    def display(self): # self is used to access the current object's data #here the behaviour is given of object
        print(f'ID:{self.id}\t NAME:{self.name}\t SAL:{self.sal}')# self.id, self.name and self.sal access the values stored in the object
e1=employee(1,'Yash',12000)#here object is created 
e2=employee(2,'Sakshi',120000)#here object is created
e1.display()
e2.display()
e1.display()
# e1.name="Viarat"
e1.setName("Virat")#set used to chnge name
e1.display()
print(e2.getSal())#to access salary
e2.setSal(12121212)
print(e2.getName()," ",e2.getSal())
