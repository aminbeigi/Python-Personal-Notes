# Pythonic Tips and Tricks

## Merging Lists
You can use single star/asterisk `*` to **unpack argument lists**.

```py
>>> even = [i for i in range(1, 11, 2)]
>>> odd = [i for i in range(1, 11, 3)]
>>> nums = [*even, *odd]
>>> nums
[1, 3, 5, 7, 9, 1, 4, 7, 10]
```

## Merging Dictionaries
You can use double star/asterisk `**` to **unpack argument key value pairs**.

```py
>>> fruits = {'apple': 1, 'tomato': 2}
>>> vegetables = {'tomato': 3, 'broccoli': 4}
>>> food = {**fruits, **vegetables}
>>> food
{'apple': 1, 'tomato': 3, 'broccoli': 4}
```

## Testing Multiple Flags
```py
x, y, z = 0, 1, 0
if x == 1 or y == 1 or z == 1:
    pass
if 1 in (x, y, z):
    pass

# these only test for truthy:
if x or y or z:
    pass
if any((x, y, z)):
    pass
```

## String Splicing
```py
>>> s = 'Bruce Wayne'
>>> s[:3]
'Bru'
>>> s[:-3]
'Bruce Wa'
>>> s[3:]
'ce Wayne'
>>> s[-3:]
'yne'
>>> s[-1]
'e'
>>> s[::-1]
'enyaW ecurB'
```

## String Character Check
`any` takes in an iterable as its only argument and will return true if atleast one element of given iterable is true.
```py
>>> password = 'carr0t33'
>>> any(c.isdigit() for c in password)
True
>>> any(c.islower() for c in password)
True
>>> any(c.isupper() for c in password)
False
```
