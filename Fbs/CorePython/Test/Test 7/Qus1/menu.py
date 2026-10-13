from bookmng import Bookmanage

obj = Bookmanage()

while True:
    print("\n----- BOOK MANAGEMENT SYSTEM -----")
    print("1. Add Book")
    print("2. Delete Book")
    print("3. Display All Books")
    print("4. Search Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.addbook()

    elif choice == 2:
        obj.deletebook()

    elif choice == 3:
        obj.displaybook()

    elif choice == 4:
        obj.searchbook()

    elif choice == 5:
        print("Thank you for using Book Management System!")
        break

    else:
        print("Invalid choice! Please try again.")