class Vehicle:
    lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")
class Car(Vehicle):
    def __init__(self):
        print("Car")
class Pickup(Vehicle):
    def __init__(self):
        print("Pickup")
class Van(Vehicle):
    def __init__(self):
        print("Van")
car1 = Car()
car1.turnOnAirConditioner()
pickup1 = Pickup()
pickup1.turnOnAirConditioner()
van1 = Van()
van1.turnOnAirConditioner()