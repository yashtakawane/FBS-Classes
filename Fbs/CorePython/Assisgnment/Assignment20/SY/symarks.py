class SYMARKS:
    def __init__(self,ComputerTotal,MathsTotal, ElectronicsTotal):
        self.ComputerTotal=ComputerTotal
        self.MathsTotal=MathsTotal
        self.ElectronicTotal=ElectronicsTotal

    def getComputerTotal(self):
        return self.ComputerTotal
    def setComputerTotal(self,newComputer):
        self.ComputerTotal=newComputer

    def getMathsTotal(self):
        return self.MathsTotal
    def setMathsTotal(self,newMath):
        self.MathsTotal=newMath

    def getElectronicTotal(self):
        return self.ElectronicTotal
    def setElectronicTotal(self,newElec):
        self.ElectronicTotal=newElec




