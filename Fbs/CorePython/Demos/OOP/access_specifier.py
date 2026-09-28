class Emp:
    def __init__(self,id,name,sal):
        self.id= id #public: Everywhere in code
        self._name = name #protected: Available in class and subclass
        self.__sal= sal #private: only available inside class

e1=Emp(101,'ABC',50000)
print(e1.id)
print(e1._name)#   not work in python
#print(e1.__sal) # raise error
print(e1._Emp__sal)