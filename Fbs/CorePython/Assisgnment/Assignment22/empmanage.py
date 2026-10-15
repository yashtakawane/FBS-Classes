
import pickle
from emp import Emp

FILENAME = "employee.dat"


class EmpManage:

    def readRecords(self):
        try:
            with open(FILENAME, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    def saveRecords(self, records):
        with open(FILENAME, "wb") as f:
            pickle.dump(records, f)


    def addRecord(self):
        eid = int(input("Enter Employee ID: "))

        records = self.readRecords()

        for emp in records:
            if emp.eid == eid:
                print("Employee ID already exists!")
                return

        ename = input("Enter Employee Name: ")
        basic = float(input("Enter Basic Salary: "))

        emp = Emp(eid, ename, basic)
        records.append(emp)

        self.saveRecords(records)
        print("Employee added successfully!")


    def searchRecord(self):
        eid = int(input("Enter Employee ID to search: "))
        records = self.readRecords()

        for emp in records:
            if emp.eid == eid:
                print(emp)
                return

        print("Employee not found!")

    def deleteRecord(self):
        eid = int(input("Enter Employee ID to delete: "))
        records = self.readRecords()

        for emp in records:
            if emp.eid == eid:
                records.remove(emp)
                self.saveRecords(records)
                print("Employee deleted successfully!")
                return

        print("Employee not found!")

    def editRecord(self):
        eid = int(input("Enter Employee ID to edit: "))
        records = self.readRecords()

        for emp in records:
            if emp.eid == eid:
                emp.ename = input("Enter new name: ")
                emp.basic = float(input("Enter new basic salary: "))

                self.saveRecords(records)
                print("Employee updated successfully!")
                return

        print("Employee not found!")

    def displayRecords(self):
        records = self.readRecords()

        if not records:
            print("No employee records found!")
            return

        for emp in records:
            print(emp)
