"""multithreading in Python"""

import time
"""synchronous code snippet"""
start = time.perf_counter()

def foo():
    print("Sleeping 1 second...")
    time.sleep(1)
    print('Done sleeping...')

foo()
foo()
finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)') # Finished in 2.01 second(s)


import threading
"""old way to do threading"""
start = time.perf_counter()

def foo1():
    print("Sleeping 1 second...")
    time.sleep(1)
    print('Done sleeping...')

threads = []
for _ in range(2):
    t = threading.Thread(target=foo1)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)') # Finished in 1.01 second(s)


import concurrent.futures
"""new way to do threading"""
start = time.perf_counter()

def foo3(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(foo3, secs)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)') # Finished in 5.01 second(s)