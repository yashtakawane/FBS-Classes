#Write a program which calculates toll calculation on some location following is data provided:
#Many vehicles goes through the toll every vehicle has to pay the basic toll + extra charges if any.
#two wheelers have to pay basic toll Rs 20 
# three wheelers have to pay30 and
#  four wheelers have to pay 40
#heavy veheicles i.e. Vehicles having wheels more than four, have to pay 60 Rs as basic toll
#extra charges :
#for two wheelers if no. of persons are more than two extra charge=10/person
#for three wheelers if no. of persons are more than 3 extra charge=20/person
#for four wheelers if no. of persons are more than 4 extra charge=40/person
#for heavy vehicle if no. of person are more than 6 extra charges=100/person.
#Show polymorphic behaviour in main. Main module should be
#designed in such way that toll should easily operate it through interactive menu driven program .#

class Vehicle:
    def __init__(self, passenger):
        self.passenger = passenger

    def toll(self):
        pass


class TwoWheeler(Vehicle):
    def toll(self):
        toll = 20

        if self.passenger > 2:
            extra_passenger = self.passenger - 2
            toll = toll + (10 * extra_passenger)

        return toll


class ThreeWheeler(Vehicle):
    def toll(self):
        toll = 30

        if self.passenger > 3:
            extra_passenger = self.passenger - 3
            toll = toll + (20 * extra_passenger)

        return toll


class FourWheeler(Vehicle):
    def toll(self):
        toll = 40

        if self.passenger > 4:
            extra_passenger = self.passenger - 4
            toll = toll + (40 * extra_passenger)

        return toll


class HeavyVehicle(Vehicle):
    def toll(self):
        toll = 60

        if self.passenger > 6:
            extra_passenger = self.passenger - 6
            toll = toll + (100 * extra_passenger)

        return toll

while True:

    print("\n===== TOLL MENU =====")
    print("1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Thank you!")
        break

    passenger = int(input("Enter number of passengers: "))

    if choice == 1:
        vehicle = TwoWheeler(passenger)

    elif choice == 2:
        vehicle = ThreeWheeler(passenger)

    elif choice == 3:
        vehicle = FourWheeler(passenger)

    elif choice == 4:
        vehicle = HeavyVehicle(passenger)

    else:
        print("Invalid choice!")
        continue

    print("Total Toll =", vehicle.toll())    
