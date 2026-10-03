# decoretor(login)
def decoretor(a):
    def wrapper(*args):
        print("Time Started")
        print("Logger removed")
        a(*args)
        print("Time Stopped")
        print("Logger removed")
    return wrapper

@decoretor
def login():
    print('\nLogIn is done\n')
login()

@decoretor
def add(a,b):
    print(a+b)

add(10,20)