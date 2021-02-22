"""Tips and Tricks"""

"""merging dictionaries"""
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y} # z = {'a': 1, 'b': 3, 'c': 4} 

"""testing multiple flags"""
x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    pass
if 1 in (x, y, z):
    pass
# These only test for truthiness:
if x or y or z:
    pass
if any((x, y, z)):
    pass

"""string splicing"""
string = 'Batman'
string[:2]  # 'Ba'
string[:-2]  # 'Batm'

string[2:]  # 'tman'
string[-2:]  # 'an'

string[-1]   # 'n'
string[::-1] # 'namtaB'

"""string character check"""
password = 'carr0t33'
any(c.isdigit() for c in password) # True
any(c.islower() for c in password) # True
any(c.isupper() for c in password) # False