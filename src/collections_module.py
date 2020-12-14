"""built-in collections module 

The collections modules has some super cool stuff such as the namedtuple module - which
is like the struct in C.
"""

from collections import namedtuple
# example 1
Color = namedtuple('Color', ['red', 'green', 'blue'])
lime = Color(75, 100, 0)
lime # Color(red=75, green=100, blue=0)
lime[0], lime.red # 75, 75

# example 2
Point = namedtuple('Point', ['x', 'y', 'z'])
p = Point(11, 74, None) # Point(x=11, y=74, z=None)
p # Point(x=11, y=74, z=None)