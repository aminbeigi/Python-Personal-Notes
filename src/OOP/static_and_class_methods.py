"""Static and Class Methods"""

class Person:
    population = 5250
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1
    
    """instance method
    takes self as a parameter, which points to an instance of Person
    """
    def get_name(self):
        return self.name

    """class methods
    takes cls as a parameter, that points to Person not the object instance
    """
    @classmethod
    def get_population(cls):
        return cls.population

    """static methods
    can neither modify object state nor Person's state
    """
    @staticmethod
    def is_adult(age):
        return age >= 18

person = Person('Bob', 18)
Person.get_population() # 5251
Person.is_adult(18) # True