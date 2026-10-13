from book import Book

class Bookmanage:
    bookdetail={}
    def addbook(self):
        bid=input("Enter Book Id: ")
        if bid in Bookmanage.bookdetail:
            print("Book is Aalredy Exist...")
            return
        else:
            bname=input("Enter the Book Name= ")
            bprice=float(input("Enter Book price = "))
            bauthor=input("Enter the Book Author= ")
        Bookmanage.bookdetail[bid]=Book(bid, bname, bprice, bauthor)
        print("Book added sussefully....")

    def deletebook(self):
        bid = input("Enter Book Id to delete: ")

        if bid in Bookmanage.bookdetail:
            Bookmanage.bookdetail.pop(bid)
            print("Book deleted successfully...")
        else:
            print("Book not found...")

    def displaybook(self):
        if len(Bookmanage.bookdetail) == 0:
            print("No books available...")
            return

        for bid in Bookmanage.bookdetail:
            print(Bookmanage.bookdetail[bid])

    def searchbook(self):
        bid = input("Enter Book Id to search: ")

        if bid in Bookmanage.bookdetail:
            print(Bookmanage.bookdetail[bid])
        else:
            print("Book not found...")