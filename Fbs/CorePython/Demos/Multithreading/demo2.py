from time import sleep
from threading import Thread

class Demo1(Thread):
    def run(self):
        for i in range(5):
            print("Pizza")
            sleep(1)

class Demo2(Thread):
    def run(self):
        for i in range(5):
            print("Burger")
            sleep(1)

t1=Demo1()
t2=Demo2()
t1.start()
t2.start()
t1.join()
t2.join()
print("------------------I am in main thread-----------------------")