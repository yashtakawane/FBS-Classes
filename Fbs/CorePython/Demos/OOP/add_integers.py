class sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

a = int(input("Enter number one:"))
b = int(input("Enter number two:"))

result = sum(a, b)
print("The sum of", a, "and", b, "is", result.add())