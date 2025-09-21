##Thomas Cubstead
##OOP Review Project
##Parking_Ticket_Sim 
##9/21/25
##This program simulates a parking ticket scenario using OOP principles.

import math

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

        @minutes_parked.setter
        def minutes_parked(self, value):
            if value < 0:
                raise ValueError("Minutes parked cannot be negative.")
            self._minutes_parked = value

        def __str__(self):
            return f"{self.color} {self.make} {self.model}, License: {self.license_number}, Minutes Parked: {self.minutes_parked}"

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

