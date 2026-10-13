# Create class television that has members to hold the model number ,screen sizeand price.
# Take a member function to take input from user, 
# If more than 4 digitsare entered for model number, 
# if screen size is smaller than 12 inches or greater
# than 70 inches or if the price is negative or greater than 5000 Rs, then throw an exception.
# Write a main() that instantiates an object and allows the user to enter and display data. 
# If exception is caught, replace all data member values with zero

class Television:
    def __init__(self):
        self.model = 0
        self.screen_size = 0
        self.price = 0

    def getData(self):
        self.model = int(input("Enter model number: "))
        if self.model < 0 or self.model > 9999:
            raise ValueError("Model number must have at most 4 digits")

        self.screen_size = float(input("Enter screen size: "))
        if self.screen_size < 12 or self.screen_size > 70:
            raise ValueError("Screen size must be between 12 and 70")

        self.price = float(input("Enter price: "))
        if self.price < 0 or self.price > 5000:
            raise ValueError("Price must be between 0 and 5000")

    def display(self):
        print("\n--- Television Details ---")
        print("Model Number:", self.model)
        print("Screen Size:", self.screen_size)
        print("Price:", self.price)