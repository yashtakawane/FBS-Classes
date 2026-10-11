from time import sleep
from threading import Thread,Lock

class Bank:
    balance=1000
    l1=Lock()
    def withdraw(self,amount):
        Bank.l1.acquire()
        if amount< Bank.balance:
            print(f"Processing withdraw of {amount}")
            oldbalance=Bank.balance
            sleep(1)
            Bank.balance= oldbalance - amount
            
            print(f"{amount} got withdraw")
        else:
            print(f"Incufficient balance for {amount}")

        Bank.l1.release()

        
b=Bank()
t1=Thread(target=b.withdraw,args={700})
t2=Thread(target=b.withdraw,args={500})
t1.start()
t2.start()
t1.join()
t2.join()
print(f"final balance={Bank.balance}")