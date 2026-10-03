class MyException(Exception):
    def __init__(self, *args):
        self.age=args
        print("I am in Con of MyException Class")
    def __str__(self):
        return 'Enter Valid Age!'