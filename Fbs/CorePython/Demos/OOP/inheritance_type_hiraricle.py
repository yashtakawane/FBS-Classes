class Emp:
    def __init__(self,nm):
        self.name=nm
    def display(self):
        print('Display')

class dev(Emp):
    def display(self):
        print('Display of developer')
     
class HR(Emp):
    def display(self):
        print("display of HR")

class JrHr(HR):
    def display(self):
        print('I am from display of jr Hr')

class SrHr(HR):
    def display(self):
        print('I am from display of Sr Hr')

class Jrdev(dev):
    def display(self):
        print('Display of Junior developer')


class Srdev(dev):
    def display(self):
        print('Display of Senior developer')

jhr=JrHr('Yash')
jhr.display() 
Jrd=Jrdev('Sakshi')
Jrdev.display()