# 1. Using Modules concept
# Create a class to store book details (bid, name, price and author).
# Write a menu driven program with following options:
# a. Add Book
# b. Delete book by id
# c. Display all books
# d. Search book by id
# Use dictionary to store all information.

class Book:
    def __init__(self,bid,name,price,author):
        self.bid=bid
        self.name=name
        self.price=price
        self.author=author

    def getbid(self):
        return self.bid
    def setid(self,newid):
        self.bid=newid

    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname

    def getprice(self):
        return self.price
    def setprice(self,newprice):
        self.price=newprice

    def getauthor(self):
        return self.author
    def setauthor(self,newauthor):
        self.author=newauthor

    def __str__(self):
        return f'ID:{self.bid}\t Name:{self.name}\t Price={self.price}\t Author={self.author}'

    

    
        

# b1=Book()