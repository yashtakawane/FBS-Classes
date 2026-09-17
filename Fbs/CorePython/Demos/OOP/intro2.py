class Student():
    inName='FBS'
    stdCount=0#to count number of students
    @staticmethod #used to pass static method or variable ##@staticmethode should be passed every time before ststic method
    def getinName():
        return Student.inName
    @staticmethod
    def setinName(nm):
          Student.inName=nm

          
    def __init__(self,rollno,name,batch):
        self.rollno=rollno
        self.name=name
        self.batch=batch
        Student.stdCount+=1
    def display(self):
        print(f'RollNo:{self.rollno}\t Name:{self.name}\t Batch:{self.batch}\t Institue:{Student.inName}')

    def getrollno(self): #getter and setter are used to access or change state by behaviour as state is hidden in real
            return self.rollno
    def setrollno(self,newrollno):
            self.rollno=newrollno
        
            
    def getname(self):
            return self.name
    def setname(self,newname):
            self.name=newname
        
            
    def getbatch(self):
            return self.batch
    def setbatch(self,newbatch):
            self.batch=newbatch
        
s1=Student(1,'Yash','July Python')
s2=Student(2,'Sakshi','July Java')
s1.display()
s2.display()
#s1.setmarks(99)
#print(s2.getname())
Student.inName='FirstBit Solution'
print('-------------------------------------------------------------')
s1.display()
s2.display()
Student.setinName('Zeal')
print(Student.inName)
s1.display()
s2.display()
print(f'The number of students are {Student.stdCount}')