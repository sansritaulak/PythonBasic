class Vehicle:
    def general_usage(self):
        print("General use: Transportation")
    
#Derive class Car from class Vehicle    
class Car(Vehicle):
    def __init__(self):
        print("I am car.")
        self.wheels = 4
        self.has_roof = True
   
    def specific_usage(self):
        print("Specific use: Commute to work, vacation with family")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I am motor cycle.")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print("Specific use: Road trip, Racing") 

#calling the derived classes using objects
c = Car()
c.general_usage()
c.specific_usage()

m = MotorCycle()
c.general_usage()
c.specific_usage()

#isinstance() tells if a object is the instance of the class or not 
print(isinstance(c,Car))

#issubclass() tells if a class is a sub class of another class or not 
print(issubclass(Car,Vehicle))