##Thomas Cubstead
##OOP Review Project
##Parking_Ticket_Sim 
##9/21/25
##This program simulates a parking ticket scenario using OOP principles

import math

#holds car info
class ParkedCar:
    def __init__(self, make, model, color, license_number, minutes_parked=60):
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self.minutes_parked = 60
        self.minutes_parked = minutes_parked

        @property
        def minutes_parked(self):
            return self._minutes_parked

        #setter with validation
        @minutes_parked.setter
        def minutes_parked(self, value):
            if value < 0:
                raise ValueError("Minutes parked cannot be negative.")
            self._minutes_parked = value
        #output formatting
        def __str__(self):
            return f"{self.color} {self.make} {self.model}, License: {self.license_number}, Minutes Parked: {self.minutes_parked}"

#holds purchased time
class ParkingMeter:
    def __init__(self, minutes_purchased=60):
        self._minutes_purchased = 60
        self.minutes_purchased = minutes_purchased

    @property
    def minutes_purchased(self):
        return self._minutes_purchased

    @minutes_purchased.setter
    def minutes_purchased(self, value):
        if value <= 0:
            raise ValueError("Minutes purchased must be more than zero.")
        self._minutes_purchased = value

#formatting for tickets
class ParkingTicket:
    def __init__(self, car, officer, illegal_minutes):
        self.car = car
        self.officer_name = officer.name
        self.badge_number = officer.badge_number
        self.illegal_minutes = illegal_minutes
        self.fine = self.calculate_fine()
    
    #calculates fine based on illegal minutes
    def calculate_fine(self):
        hours = math.ceil(self.illegal_minutes /60)
        if hours <= 1:
            return 25.0
        else:
            return 25.0 + (hours - 1) * 10.0

    #output 
    def __str__(self):
        return (f"=== PARKING TICKET ===\n"
                f"Car: {self.car.make} {self.car.model}, color: {self.car.color}, license: {self.car.license_number}\n"
                f"Illegally Parked for: {self.illegal_minutes} minutes\n"
                f"Fine: ${self.fine:.2f}\n"
                f"Issued by officer: {self.officer_name}, Badege #: {self.badge_number}\n")

#compares parked time to purchased time and issues ticket if necessary
class PoliceOfficer:
    #officer info
    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number

    #determines wether or not to issue a ticket
    def inspect_car(self, parked_car, parking_meter):
        parked_time = parked_car.minutes_parked
        purchased_time = parking_meter.minutes_purchased

        if parked_time > purchased_time:
            illegal_minutes = parked_time - purchased_time
            return ParkingTicket(parked_car, self, illegal_minutes)
        else:
            return None

#test cases
def scenario1():
    print("Scenario 1: Legally Parked Car")
    car = ParkedCar("Toyota", "Camry", "Red", "XYZ123", 30)
    meter = ParkingMeter(40)
    officer = PoliceOfficer("John Doe", "5678")

    ticket = officer.inspect_car(car, meter)
    if ticket:
        print(ticket)
    else:
        print("No ticket issued. Car is legally parked.\n")

def scenario2():
    print("Scenario 2: Car Parked Illegally (Less Than an Hour Over)")
    car = ParkedCar("Honda", "Accord", "Blue", "ABC987", 70)
    meter = ParkingMeter(60)
    officer = PoliceOfficer("Jane Smith", "1234")

    ticket = officer.inspect_car(car, meter)
    if ticket:
        print(ticket)
    else:
        print("No ticket issued. Car is legally parked.\n")

def scenario3():
    print("Scenario 3: Car Parked Illegally (Multiple Hours Over)")
    car = ParkedCar("Ford", "Mustang", "Black", "LMN456", 190)
    meter = ParkingMeter(60)
    officer = PoliceOfficer("James Brown", "4321")

    ticket = officer.inspect_car(car, meter)
    if ticket:
        print(ticket)
    else:
        print("No ticket issued. Car is legally parked.\n")

def scenario4():
    print("Scenario 4: Multiple Cars in a Parking Lot")
    cars = [
        (ParkedCar("Nissan", "Altima", "White", "JKL321", 60), ParkingMeter(60)),
        (ParkedCar("Chevy", "Malibu", "Silver", "QWE789", 80), ParkingMeter(60)),
        (ParkedCar("BMW", "X5", "Black", "BMW999", 500), ParkingMeter(60)),
        (ParkedCar("Mazda", "3", "Blue", "MAZ321", 45), ParkingMeter(60)),
    ]
    officer = PoliceOfficer("Sarah Green", "9999")

    for car, meter in cars:
        ticket = officer.inspect_car(car, meter)
        if ticket:
            print(ticket)
        else:
            print(f"No ticket issued for {car.make} {car.model} ({car.license_number}). Car is legally parked.\n")


# ------------------------------
# Main Execution
# ------------------------------
if __name__ == "__main__":
    scenario1()
    print("-" * 50)
    scenario2()
    print("-" * 50)
    scenario3()
    print("-" * 50)
    scenario4()




