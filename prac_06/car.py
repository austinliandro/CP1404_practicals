"""
CP1404 Practical - Austin Liandro
Car class
"""


class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        """It will load a car instance."""
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def __str__(self):
        """It will return the string representation of a car object."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"

    def add_fuel(self, amount):
        """To add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """It will give the distance when driving the car"""
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance