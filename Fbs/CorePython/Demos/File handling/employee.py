import pickle
class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def getName(self): 
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


    def __str__(self):
        return (f'Id:{self.id}\t Name:{self.name}\t Salary:{self.salary}')

    
e1= Employee(1,"Yash",500000)
e2= Employee(2,"Raj",300000)
e3= Employee(3,"Don",200000)

# with open("employee.txt","w") as f:
#     f.write(str(e1))
#     f.write(str(e2))
#     f.write(str(e3))
# it is easy to write but reading every object can increase time and space complexity
#so pickling is used

f=open("emp.dat","wb")
print(f.tell())#used to find the position of the cursor
##pickle.dump("Objectname","Object")
pickle.dump(e1,f)#used to convert in bit string and store
pickle.dump(e2,f)
pickle.dump(e3,f)

fr=open("emp.dat","rb")
f.seek(0)#seek()is used to change the position of the cursor
data=pickle.load(fr)
# print(data.getId()) #use to get 
# data.setName("Sakshi")#use to set
data1=pickle.load(fr)
data2=pickle.load(fr)
print(data)
print(data1)
print(data2)