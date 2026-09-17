class Car():
    inName='Fourwheeler'
    stdCount=0#to count number of students
    @staticmethod #used to pass static method or variable ##@staticmethode should be passed every time before ststic method
    def getinName():
        return Car.inName
    @staticmethod
    def setinName(nm):
         Car.inName=nm
    

    def __init__(self,brand,name,prize):
        self.brand=brand
        self.name=name
        self.prize=prize
    def display(self):
        print(f'BRAND:{self.brand}\t NAME:{self.name}\t PRIZE:{self.prize}\t Type:{Car.inName}')

    def getbrand(self):
        return self.brand
    def setbrand(self,newbrand):
        self.brand=newbrand

    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname

    def getprize(self):
        return self.prize
    def setprize(self,newprize):
            self.prize=newprize
        
        
    
c1=Car("Mercedise","G63",1200000)
c2=Car("Volkvagoan","Virtus",2100000)
c1.display()
c2.display()
c1.setname('AMG')
c1.display()
c2.getname()
