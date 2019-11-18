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

    def showDetails(self):
        print(f"Id is {self.id}")
        print(f"Name is {self.name}")
        print(f"Fuel Type is {self.fuelType}")
        print(f"Transmission type is {self.transmissionType}")
        print(f"Seats is {self.seats}")
        self.carDetails.append( [self.id, self.name, self.fuelType, self.transmissionType, self.seats] )
        self.testFn(self.carDetails)

    def testFn(*details):
        print(*details)

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

print(myNewCar.id)
print(myNewCar.name)
print(myNewCar.fuelType)
print(myNewCar.transmissionType)
print(myNewCar.seats)

print(myNewCar.__dict__)
print(myNewCar.showDetails())