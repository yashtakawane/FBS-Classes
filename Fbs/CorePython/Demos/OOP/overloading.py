class Time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec

    def gethr(self):
        return self.hr
    def sethr(self,newhr):
        self.hr=newhr
    def getmin(self):
        return self.min
    def sethr(self,newmin):
        self.min=newmin
    def getsec(self):
        return self.sec
    def setsec(self,newsec):
        self.sec=newsec

    def __str__(self): #this method is used to return when only object is called
        return (f'Hours:{self.hr}\t Minutes:{self.min}\t Secounds{self.sec}')

    def __add__(self,other):#in this method overloading is done and this is called overriding
        tsec=self.sec+other.sec
        addmin=tsec//60
        tsec=tsec%60
        tmin=self.min+other.min+addmin
        addhr=tmin//60
        tmin=tmin%60
        thr=self.hr+other.hr+addhr
        return  (f'Hours:{thr}\t Minutes:{tmin}\t Secounds{tsec}')
hr=int(input('Enter hours:'))
min=int(input('Enter Minuets:'))
sec=int(input('Enter Secounds:'))
t1=Time(hr,min,sec)


hr1=int(input('Enter hours:'))
min1=int(input('Enter Minuets:'))
sec1=int(input('Enter Secounds:'))
t2=Time(hr1,min1,sec1)
#print(t1)#calling only object gives a readable out because of __str__() method
print(t1+t2)