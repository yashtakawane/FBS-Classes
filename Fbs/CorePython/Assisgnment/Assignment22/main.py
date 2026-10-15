import pickle
from empmanage import EmpManage

obj = EmpManage()

while True:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            obj.addRecord()

        elif choice == 2:
            obj.searchRecord()

        elif choice == 3:
            obj.deleteRecord()

        elif choice == 4:
            obj.editRecord()

        elif choice == 5:
            obj.displayRecords()

        elif choice == 6:
            print("Thank you!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter valid numeric input.")

    except (OSError, pickle.UnpicklingError) as e:
        print("File error:", e)
