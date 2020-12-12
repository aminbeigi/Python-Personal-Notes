"""Tips and Tricks

Includes some smaller pythonic stuff.
"""

""" merging dictionaries
overwriting duplicates from left to write
z = {'a': 1, 'b': 3, 'c': 4} 
"""
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}