class Mec():
    def display(self):
        print('Mec')
class Electric():
    def display(slef):
        print('Electrical')
class Mecatronix(Mec,Electric):
    def abc():
        print('Mectronix')
m=Mecatronix()
m.display()#now here in mectronix display is not present so it will take it from subclasses and priority to the class which is first written