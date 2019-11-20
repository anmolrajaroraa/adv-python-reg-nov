class Car:
    """This class is used to make new car objects"""
    cars = []

    def __init__( self ):     #magic method -> it automatically gets invoked when a new object is created, we dont need to call __init__
        self.id = None
        self.name = None
        self.fuelType = None
        self.transmissionType = None
        self.seats = None
        self.carDetails = []
    
    def __str__( self ):
        # return f"{self.id},{self.name},{self.fuelType},{self.transmissionType},{self.seats}"
        return str(self.__dict__)

    def __del__( self ):
        print(f"Object {self.name} deleted")

    def showDetails( self ):
        self.carDetails.extend([self.id, self.name, self.fuelType, self.transmissionType, self.seats])
        self.cars.append(self.carDetails)
        print(self.carDetails)

myCar = Car()
myCar.id = 101
myCar.name = 'hector'
myCar.fuelType = 'diesel'
myCar.transmissionType = 'A'
myCar.seats = 7
myCar.showDetails()

myNewCar = Car()
myNewCar.id = 102
myNewCar.name = 'seltos'
myNewCar.fuelType = 'cng'
myNewCar.transmissionType = 'A'
myNewCar.seats = 5
myNewCar.showDetails()

# print(myNewCar.cars)
print(myCar)
print(myNewCar)