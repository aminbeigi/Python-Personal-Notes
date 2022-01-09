# Dataclasses and Named Tuples
## Dataclass
Data classes are just regular classes that are geared towards storing state, rather than containing a lot of logic. Every time you create a class that mostly consists of attributes, you make a data class.

What the dataclasses module does is to make it easier to create data classes. It takes care of a lot of boilerplate for you.
This is especially useful when your data class must be hashable; because this requires a `__hash__` method as well as an `__eq__` method. If you add a custom `__repr__` method for ease of debugging, that can become quite verbose:

```py
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity: int = 0

    def __init__(self, name: str, unit_price: float, quantity: int = 0) -> None:
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

    def total_cost(self) -> float:
        return self.unit_price * self.quantity
    
    def __repr__(self) -> str:
        return (
            'InventoryItem('
            f'name={self.name!r}, unit_price={self.unit_price!r}, '
            f'quantity={self.quantity!r})'

    def __hash__(self) -> int:
        return hash((self.name, self.unit_price, self.quantity))

    def __eq__(self, other) -> bool:
        if not isinstance(other, InventoryItem):
            return NotImplemented
        return (
            (self.name, self.unit_price, self.quantity) == 
            (other.name, other.unit_price, other.quantity))
```

With `dataclasses` you can reduce it to:

```py
from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```
## Named tuples
`namedtuple` is a module inisde the built-in `collections` package. `namedtuple` classes are also data classes which are immutable.
Named tuples basically add metadata to tuples, in the form of naming what each field does, and otherwise acts as a tuple.


Say we wanted to store colours in RGB format in a tuple. We could use a data class but lets store our information in a tuple.
For example, let us store the colour lime:
```py
>>> Color = namedtuple('Color', ['red', 'green', 'blue'])
>>> lime = Color(75, 100, 0)
>>> lime
Color(red=75, green=100, blue=0)
>>> lime.red
75
```

## Why would I use `namedtuple` over a dataclass?
* Tuples are more efficient than dataclasses (but of course contain less information).

## Acknowledgement
https://stackoverflow.com/questions/47955263/what-are-data-classes-and-how-are-they-different-from-common-classes