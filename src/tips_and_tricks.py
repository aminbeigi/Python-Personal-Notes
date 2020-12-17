"""Tips and Tricks

Includes some smaller pythonic stuff.
"""

""" merging dictionaries
overwriting duplicates from left to write
"""
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y} # z = {'a': 1, 'b': 3, 'c': 4} 

""" testing multiple flags """
x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print('passed')

if 1 in (x, y, z):
    print('passed')

# These only test for truthiness:
if x or y or z:
    print('passed')

if any((x, y, z)):
    print('passed')
