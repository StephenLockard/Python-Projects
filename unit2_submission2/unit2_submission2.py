class Vehicle:
    def __init__(self):
        self.color = None
        self.horse_power = None
        self.engine = None
        self.vehicle_price = None

    def set_vehicle(self):
        self.color = input("What is the color of the vehicle?")
        self.horse_power = input("What is the horse power of the vehicle?")
        self.engine = input("The engine type for the vehicle:")
        self.vehicle_price = input("The price for the vehicle:")


class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.number_of_doors = None
        self.is_convertible = None

    def set_car(self):
        self.number_of_doors = input("Number of doors on the car?")
        self.is_convertible = input("Is the car a convertible?")


class Truck(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.number_of_doors = None
        self.number_of_wheels = None
        self.has_flatbed = None

    def set_truck(self):
        self.number_of_doors = input("Number of doors on the truck?")
        self.number_of_wheels = input("Number of wheels on the truck?")
        self.has_flatbed = input("Does the truck have a flatbed?")


class Boat(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.has_top = None
        self.length = None

    def set_boat(self):
        self.has_top = input("Does the boat have a top?")
        self.length = input("What is the length of the boat?")


car = Car()
car.set_vehicle()
car.set_car()
truck = Truck()
truck.set_vehicle()
truck.set_truck()
boat = Boat()
boat.set_vehicle()
boat.set_boat()
