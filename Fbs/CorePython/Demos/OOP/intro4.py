class Teacher():
    def __init__(self,id,name,subject):
        self.id=id
        self.name=name
        self.subject=subject
    def display(self):
        print(f'ID:{self.id}\t Name:{self.name}\t Subject:{self.subject}')

    def getid(self):
        return self.id
    def setid(self,newid):
        self.id=newid
    
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname
    
    def getsubject(self):
        return self.subject
    def setsubject(self,newsubject):
        self.subject=newsubject
        
t1=Teacher(1,"Pradip","OOP")
t2=Teacher(2,'Randeep',"Python")
t1.display()
t2.display()
t1.setname('Vineet')
t1.display()
print(t2.getid())