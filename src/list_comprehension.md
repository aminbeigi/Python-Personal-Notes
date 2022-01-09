# List Comprehension
List comprehension is an elegant way to define and create lists.
Faster than regular functions and loops for creating lists.

All examples below will return: 
```py
lst = [0, 'odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd', 10, 'odd', 12, 'odd', 14]
```

First, the "full" for loop:
```py
lst = []
for i in range(15):
    if i%2 == 0:
        lst.append(i)
    else:
        lst.append("odd")
```

Lambda map (functional programming):
```py
lst = list(map(lambda i: i if i%2==0 else "odd", range(15)))
```

List comprehension:
```py
lst = [i if i % 2 == 0 else "odd" for i in range(15)]
```