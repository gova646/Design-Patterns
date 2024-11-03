from bike import Bike
from car import Car

class NoVehicleException(Exception):
    pass

class VehicleFactory:
    def getVehicle(self,vehicleType):
        if vehicleType.lower() == 'bike':
            return Bike()
        elif vehicleType.lower() == 'car':
            return Car()
        else:
            raise NoVehicleException('No vehicle of such type. Please request for implementation')