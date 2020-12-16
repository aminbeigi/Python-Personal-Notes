import time

""" Decorators 

A simple example of a decorator that is used to calculate the runtime of a function.
"""

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        end = time.time()
        run_time = end - start
        print(f"Finished running {func.__name__} in {run_time} seconds.")
        return rv

    return wrapper

@timer
def waste_time(num):
    for _ in range(num):
        sum([i**2 for i in range(10000)])

waste_time(1000) # Finished running waste_time in 2.9801082611083984 seconds.