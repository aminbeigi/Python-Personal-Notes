"""Property decorator

Python programming provides us with a built-in @property decorator which
makes usage of getter and setters much easier in Object-Oriented Programming.
"""

class Celsius:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError('Temperature below -273 is not possible')
        self._temperature = value

celcius = Celsius(55)

celcius.temperature # 55
celcius.temperature = 10
celcius.temperature # 10