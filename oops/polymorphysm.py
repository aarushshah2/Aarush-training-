class Car:
    def move(self):
        print("Car drives")

class Boat:
    def move(self):
        print("Boat sails")

for vehicle in (Car(), Boat()):
    vehicle.move()
