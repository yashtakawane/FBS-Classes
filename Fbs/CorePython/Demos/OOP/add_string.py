class string:
    def __init__(self,str1,str2):
        self.string1=str1
        self.string2=str2

    def sum(self):
        return self.string1 + self.string2
str1=input('Enter the string 1:')
str2=input('Enter the string 2:')
s1=string(str1,str2)
print(f'The sum of {str1} and {str2} is {s1.sum()}')
                