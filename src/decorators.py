import time

""" Decorators 

A simple example of a decorator that is used to calculate time time a function took to execute.
"""

def func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        
        end = time.time()
        print("Time:", end-start)
        return rv

    return wrapper

@func
def func2(x, y):
    time.sleep(1)
    print(f"{x} and {y} are cool")

@func
def func3():
    for _ in range(1000000):
        pass

func2('cats', 'dogs') # Time: 1.0083093643188477
func3() # Time: 0.020990848541259766