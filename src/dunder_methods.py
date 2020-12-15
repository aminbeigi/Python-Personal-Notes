"""Dunder methods"""

class Car:
    def __init__(self, make, year, colour):
        self.make = make
        self.year = year
        self.colour = colour
    
    """ __str__() 
    Invoked when you use an object with print statement.
    Computes the "informal" or nicely printable string representation of an object.
    """
    def __str__(self):
        return f"A {self.colour} car created in {self.year}."
    
    """ __repr__() 
    Invoked when you write an object's name on interactive python console.
    Computes the "offical" string representation of an object.
    """
    def __repr__(self):
        # type(self) => <class '__main__.Car'>
        return (f"<{self.__module__}.{type(self).__name__} object at {hex(id(self))}>")

    """ __eq__() 
    Implement == functionality on objects.
    """
    def __eq__(self, other):
            if isinstance(other, Car):
                if other.make == self.make:
                    return True

car1 = Car('Ford', 2014, 'red')
car2 = Car('Ford', 2016, 'white')

car1.__str__() # A red car created in 2014.
car1.__repr__() # <__main__.Car object at 0x1866b323fd0>
car1 == car2 # True