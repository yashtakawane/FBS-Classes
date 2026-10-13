# Create object of student class (Outside SY & TY package) having roll
# number, name, SYMakrs and TYMarks. Add the marksof SY and TY
# Computer subjects and calculate grade ("A" for >=70, "B" for >=60,
# "C" for >=50, “Pass Class” for >=40 else “Fail”) and display the result
# of the student in proper format.

from SY.symarks import SYMARKS
from TY.tymarks import TYMARKS

class Student:
    def __init__(self,rollno,name,symarks,tymarks):
        self.rollno=rollno
        self.name=name
        self.symarks=symarks
        self.tymarks=tymarks

    def calTotal(self):
        total=(self.symarks.ComputerTotal + self.tymarks.Theory + self.tymarks.Practical)
        return total

    def calPercentage(self):
        total=self.calTotal()
        percentage=total / 3
        return percentage

    def calGrade(self):
        percentage = self.calPercentage()

        if percentage >= 70:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        elif percentage >= 40:
            return "Pass Class"
        else:
            return "Fail"

    def display(self):
        print("\n------ STUDENT RESULT ------")
        print("Roll Number:", self.rollno)
        print("Name:", self.name)
        print("SY Computer Marks:", self.symarks.ComputerTotal)
        print("TY Theory Marks:", self.tymarks.Theory)
        print("TY Practical Marks:", self.tymarks.Practical)
        print("Total Marks:", self.calTotal(), "/ 300")
        print("Percentage:", self.calPercentage(), "%")
        print("Grade:", self.calGrade())

sy=SYMARKS(70,80,90)
ty=TYMARKS(90,88)

s1=Student(11,"Yash",sy,ty)
s1.display()
