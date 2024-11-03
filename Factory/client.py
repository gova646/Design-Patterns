from vehicleFactory import VehicleFactory

vehicleFactoryInstacne = VehicleFactory()
vehicle1 = vehicleFactoryInstacne.getVehicle('car')
vehicle2 = vehicleFactoryInstacne.getVehicle('bike')
vehicle1.display()
vehicle2.display()