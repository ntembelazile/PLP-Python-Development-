# Define the base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method.")

# Define the Car class that inherits from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving")

# Define the Plane class that inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying")

# Create objects of each class and call the move method
def test_movement():
    car = Car()
    plane = Plane()

    car.move()  # Outputs: Driving 
    plane.move()  # Outputs: Flying 
# Call the function to test movement
test_movement()
