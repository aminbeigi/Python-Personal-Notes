# Iterables, Iterators and Generators

## Iterators
Iterators are iterables that remember their position. For example, `open('hello.txt', 'r')` and `enumerate('hello')` return iterators.

All iterators are iterables, but not all iterables are iterators.

## Iterating manually
Iterators have a built-in method called `next()` that gets the next value and moves the iterator forward.
```python
>>> e = enumerate('abc')
>>> next(e)
(0, 'a')
>>> next(e)
(1, 'b')
>>> next(e)
(2, 'c')
>>> next(e)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(e)
StopIteration
```

Here `e` remembers its position, and every time we call `next(e)` it gives us the next element and moves forward. When it has no more values to give us, calling `next(e)` raises a StopIteration:

## Converting to iterators
There is a built-in function called `iter()` that converts anything iterable into an iterator.
```python
>>> it = iter('abc')
>>> it
<str_iterator object at 0x7f987b860160>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
Calling `iter()` on anything non-iterable gives us an error.

```python
>>> iter(123)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
```

## Checking if object is iterable or not
There is an easy way of checking if an object in python is iterable or not.

```python
>>> def is_iterable(obj):
...     try:
...         it = iter(obj)
...         print('yes')
...     except TypeError:
...         print('no')
...
>>> is_iterable(123)
no
>>> is_iterable("abc")
yes
```
Here you can observe that the integer `123` is not iterable, but `abc` is a string which is iterable so it outputs no and yes respectively.

## Generators

Let's create a generator function.
```python
>>> def print_gen_func():
...     print('start')
...     yield 1
...     print('between 1 and 2')
...     yield 2
...     print('between 2 and 3')
...     yield 3
...     print('end')

>>> print_gen_func()
<generator object print_gen_func at 0xb723d9b4>
```

Putting yield anywhere in a function makes it return a generator. Generators are iterators with some more features.

When the yield statement is hit, the program suspends function execution and returns the yielded value, waiting for us to call `next()`.  
When a function is suspended, the state of that function is saved. This includes any variable bindings local to the generator, the instruction pointer, the internal stack, and any exception handling.


```python
>>> p = gen_func()
>>> next(p)
start
1
>>> next(p)
between 1 and 2
2
>>> next(p)
between 2 and 3
3
>>> next(p)
end
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(p)
StopIteration
```

## Example 1
`yield` is useful when we want the function to output many things that making a list of them would be too slow or too memory inefficient. We can create generator expressions without building and holding the entire object in memory before iteration.

For example, say we want generate a list of people and then iterate through each person one by one.

Method one is create and populate a list first:
```python
names = ['John', 'Amy', 'Adam', 'Zoe', 'Rick', 'Jessica']
majors = ['Math', 'Engineering', 'Computer Science', 'Arts', 'Business']

def people_list(num):
    output = []
    for i in range(num):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        output.append(person)
    return output 
```

Method two is to use a generator function:
```python
def people_generator(num):
    for i in range(num):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person
```

Both of these functions can be used like this:

```python
for person in generate_people():
    # do something here
```

We compare the size of the list and the generator using `sys.getsizeof()` to get the memory size of the object (in bytes). Clearly, the generator function is significantly more memory optimsed.

```python
>>> num = 1000000
>>> people = people_list(num)
>>> sys.getsizeof(people)
8448728
>>> people = people_generator(num)
>>> sys.getsizeof(people1)
112
```

## Example 2
Another example. Reading in large files.

Method one is using a list to store contents of large csv data:
```python
def csv_reader(FILE_PATH):
    with open(FILE_PATH, 'r') as f:
        return f.read().split('\n')
```
This is not ideal because we load everything into memory at once.

Method two is using a generator function:

```python
def csv_reader1(FILE_PATH):
    for row in open(FILE_PATH, 'r'):
        yield row
```
This is better as we open the file, we yields each row instead of returning .

We can also use generator comprehension:
```python
csv_gen = (row for row in open(FILE_PATH))
```