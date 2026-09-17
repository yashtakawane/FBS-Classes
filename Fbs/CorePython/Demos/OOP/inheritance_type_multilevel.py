class Emp:
    def __init__(self,nm):
        self.name=nm
    def display(self):
        print('Display')

class HR(Emp):
    def display(self):
        print("display of HR")

class JrHr(HR):
    def display(self):
        print('I am from display of jr Hr')

jhr=JrHr('Yash')
jhr.display()