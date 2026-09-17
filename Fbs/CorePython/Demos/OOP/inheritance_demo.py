class Student():
    inName='FBS'
    stdCount=0
    @staticmethod
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

    def getrollno(self):
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

class placedStudent(Student):#Based class-Student is used in Derived class-placedStudent
    def __int__(self,rollno,name,batch,cName):
          super().__int__(rollno,name,batch)#super is used as construct chaining(used to access everything from base class to derived class)
          self.cName=cName
    def display(self):
          print(f'Company Name:{self.cName}')
          return super().display()
s1=Student(12,'Suraj',1234)
s2=placedStudent(13,'Shankr',121,'TCS')
print(Student.stdCount)
