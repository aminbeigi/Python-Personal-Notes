"""Static and Class Methods 

Instance methods need a class instance and can access the instance through self.
Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.
Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.

Use static methods when a particular method inside a class is independant to everything around it.
Flagging a method as static elucidates that a method won't modify a class or instance state.
"""

class Person:
    population = 5250
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1
    
    """ instance method
    takes self as a parameter, which points to an instance of Person
    """
    def get_name(self):
        return self.name

    """ class methods
    takes cls as a parameter, that points to Person not the object instance
    """
    @classmethod
    def get_population(cls):
        return cls.population

    """ static methods
    can neither modify object state nor Person's state
    """
    @staticmethod
    def is_adult(age):
        return age >= 18

person = Person('Bob', 18)
print(Person.get_population()) # 5251
print(Person.is_adult(18)) # True