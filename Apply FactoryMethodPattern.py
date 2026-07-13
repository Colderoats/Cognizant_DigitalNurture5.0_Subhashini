from abc import ABC, abstractmethod

# Product Interface
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


# Concrete Products
class Car(Vehicle):

    def start(self):
        return "Car started."


class Bike(Vehicle):

    def start(self):
        return "Bike started."


class Truck(Vehicle):

    def start(self):
        return "Truck started."


# Factory
class VehicleFactory:

    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type.lower() == "car":
            return Car()
        elif vehicle_type.lower() == "bike":
            return Bike()
        elif vehicle_type.lower() == "truck":
            return Truck()
        else:
            raise ValueError("Invalid vehicle type")


# Client Code
vehicle = VehicleFactory.get_vehicle("car")
print(vehicle.start())

vehicle = VehicleFactory.get_vehicle("bike")
print(vehicle.start())

vehicle = VehicleFactory.get_vehicle("truck")
print(vehicle.start())