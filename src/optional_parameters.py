"""Optional Parameters

Give parameters default values that can be overwritten.
"""

class Car(object):
    def __init__(self, make, year, colour, condition='New', mileage=0, faults=None):
        self.make = make
        self.year = year
        self.colour = colour
        self.condition = condition
        self.kms = mileage
        self.faults = faults
    
    """ __str__() 
    Invoked when you use an  object with print statement.
    Computes the "informal" or nicley printable string representation of an object.
    """
    def __str__(self):
        return f"A {self.colour} car created in {self.year}."
    
    """ __repr__() 
    Invoked when you write an object's name on interactive python console.
    Computes the "offical" string representaiotn of the object.
    """
    def __repr__(self):
        # type(self) => <class '__main__.Car'>
        return (f"<{self.__module__}.{type(self).__name__} object at {hex(id(self))}>")

car = Car('Ford', 2014, 'red', faults='Broken window.')
print(car.__str__()) # A red car created in 2014.
print(car.__repr__()) # <__main__.Car object at 0x1866b323fd0>