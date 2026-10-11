from time import sleep
from threading import Thread

def fun1():
    for i in range(5):
        print("Rohit")
        sleep(1)
def fun2():
    for i in range(5):
        print("Virat")
        sleep(1)
t1=Thread(target=fun1) #target the function which is to be thread
t2=Thread(target=fun2) 

t1.start() #starts the threat
t2.start()
t1.join() #ristrict the another thread to start until the given thread executes completly
t2.join()

print("I am in Main Thread")