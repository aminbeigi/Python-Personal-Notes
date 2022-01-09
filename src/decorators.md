# Decorators
A decorator is a function that takes another function and extends the behaviour of said function without
explicitly modifying it.

A simple example of a decorator that is used to calculate the runtime of a function:
```py
def timer(func):
    def wrapper(*args, **kwargs):
        start = time()              # before
        rv = func(*args, **kwargs)
        end = time()                # after
        runtime = end - start
        print(f"Finished running {func.__name__} in {runtime} seconds.")
        return rv
    return wrapper

@timer
def waste_time(num):
    sum([i**2 for i in range(num)])
```

Running the code:

```py
>>> waste_time(12345678)
Finished running waste_time in 2.5647943019866943 seconds.
```

We can see we are able to run code before and after the execution of the function
without explicitly modifying the original function.