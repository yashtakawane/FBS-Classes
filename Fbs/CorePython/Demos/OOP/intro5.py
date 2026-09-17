class Book():
    def __init__(self,bookname,author,price):
        self.name=bookname
        self.au=author
        self.price=price
    def display(self):
        print(f'BookName:{self.name}\t Author:{self.au}\t Price:{self.price}')
b1=Book('Rich Dad Poor Dad','Robert Kiyosaki ',200)
b2=Book('Shrimad Bhagwat Geeta Yatharoop','A.C.Bhaktivendanta Swami Prabhupada',300)
b1.display()
b2.display()