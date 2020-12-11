""" Static and Class Methods 

Instance methods need a class instance and can access the instance through self.
Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.
Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.
Static and class methods communicate and (to a certain degree) enforce developer intent about class design. This can have maintenance benefits.
"""

""" other

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
    takes self as a parameter, which points to an instance of the Person class
    """
    def get_name(self):
        return self.name

    """ class methods
    takes cls as a parameter, that points to the class not the object instance
    can't modify objects state, that would require access to self
    can modify class state that applies to all instances of the class
    """
    @classmethod
    def get_population(cls):
        return cls.population

    """ static methods
    can neither modify object state nor class state
    don't take self or cls as a parameter
    """
    @staticmethod
    def is_adult(age):
        return age >= 18

person = Person('Bob', 18)

print(Person.get_population())
print(Person.is_adult(3))