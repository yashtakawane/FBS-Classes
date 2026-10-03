# def fun(a):
#     print(a)
#------------2 step--function can be stored in variable
# def demo():
#     print('I am in demo')
# # print(type(demo))
# x=demo  # function can be stored in variable
# x()
# fun('Yash')


#----------------3 step--function can be stored as parameter to another function

# def fun(a):
#     a()

# def demo():
#     print('I am in demo')

# x=demo
# fun(x) #function can be stored as parameter too

#-----------------4 step --return one function from another function
# def outer():
#     print('I am in outer function')
#     def inner():
#         print('I am in inner function')
#     return inner
# x=outer()
# x()


#---------5th step--closer:- it is a function which pass everything to the neighbour function or inner function

# def demo():
#     a='FBS'
#     def inner():
#         print('I am in inner',a)
#     return inner
# res=demo()
# res()




#--------------Main decorater----------------

def decore(a):
    # print("I am in decorer")
    def innerfun(*args): #(*args) is used because the number of parameter is not defined
        print("Time started ")
        print("Logger added")
        a(*args)
        print("Time Stopeed")
        print("Logger removed ")
    return innerfun 
@decore
def login():
    print("Log in is Done")
    
@decore
def logout():
    print("Logout in is Done")

@decore
def add(a,b):
    print(f"Addition ={a+b}")



# res=decore(login)
# res() #instead of using these two line @decore is used

login()
logout()
add(12,23)