# class Car:
#     """This class is used to make new car objects"""
#     id = 101
#     name = 'hector'
#     fuelType = 'diesel'
#     transmissionType = 'A'
#     # seats = {'typeA':5}
#     seats = 5

class Car:
    """This class is used to make new car objects"""
    id = None
    name = None
    fuelType = None
    transmissionType = None
    seats = None
    carDetails = []

    def setCarDetails( self ):
        self.carDetails =  [self.id, self.name, self.fuelType, self.transmissionType, self.seats] 

    def showDetails(self):
        print(f"Id is {self.id}")
        print(f"Name is {self.name}")
        print(f"Fuel Type is {self.fuelType}")
        print(f"Transmission type is {self.transmissionType}")
        print(f"Seats is {self.seats}")
        # self.carDetails =  [self.id, self.name, self.fuelType, self.transmissionType, self.seats] 
        self.testFn(self.carDetails)

    def testFn(self, carDetails):
        print(carDetails)
        print(hex(id(carDetails)))

myCar = Car()
print(myCar.__class__)
print(myCar.id)
print(myCar.name)
print(myCar.fuelType)
print(myCar.transmissionType)
print(myCar.seats)
print(myCar)
print(myCar.__doc__)

# myCar.seats['typeB'] = 7
myCar.id = 101
myCar.name = 'hector'
myCar.fuelType = 'diesel'
myCar.transmissionType = 'A'
myCar.seats = 7
print(hex(id(myCar.carDetails)))
myCar.setCarDetails()

print(myCar.id)
print(myCar.name)
print(myCar.fuelType)
print(myCar.transmissionType)
print(myCar.seats)

print(myCar.__dict__)
print(myCar.showDetails())

myNewCar = Car()
myNewCar.id = 102
myNewCar.name = 'seltos'
myNewCar.fuelType = 'cng'
myNewCar.transmissionType = 'A'
myNewCar.seats = 5
myNewCar.setCarDetails()

print(myNewCar.id)
print(myNewCar.name)
print(myNewCar.fuelType)
print(myNewCar.transmissionType)
print(myNewCar.seats)

print(myNewCar.__dict__)
print(myNewCar.showDetails())
print(myCar.showDetails())

if isinstance(myNewCar,Car):
    print("myNewCar is an object of Car")