""" Optional Parameters """
# can give parameters default values

class Car(object):
    def __init__(self, make, year, colour, condition='New', mileage=0, faults=None):
        self.make = make
        self.year = year
        self.colour = colour
        self.condition = condition
        self.kms = mileage
        self.faults = faults
    
    # __str__() is invoked when you use object with print statement.
    # computes the "informal" or nicley printable string representation of an object
    def __str__(self):
        return f"A {self.colour} car created in {self.year}."
    
    # __repr__() is invoked when you write object's name on interactive python console.
    # computes the "offical" string representaiotn of the object
    def __repr__(self):
        # <__main__.Car object at 0x000001DC22091FD0>
        # self.__module__ => __main__
        # type(self) => <class '__main__.Car'>
        return (f"<{self.__module__}.{type(self).__name__} object at {hex(id(self))}>")

car = Car('Ford', 2014, 'red', faults='Broken window.')

print(car.faults)