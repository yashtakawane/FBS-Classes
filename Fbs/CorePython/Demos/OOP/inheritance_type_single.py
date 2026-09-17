class Emp:
    def __init__(self,nm):
        self.name=nm
    def display(self):
        print('Display')

class HR(Emp):
    def display(self):
        print("display of HR")

h1=HR("Yash")
h1.display()
s1=Emp('Sakshi')
s1.display()