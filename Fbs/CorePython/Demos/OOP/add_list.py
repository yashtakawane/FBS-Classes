class sum:
    def __init__(self,l1,l2):
        self.l1=l1
        self.l2=l2
    def sum(self):
        return self.l1 + self.l2

l1=list(input('Enter the list 1:'))
l2=list(input('Enter the list 2:'))
s1=sum(l1,l2)
print(f'The sum od {l1} and {l2} is {s1.sum()}')