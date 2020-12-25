import random
import sys

"""Generators - a great way to optimise memory

We can create generator expressions without buidling and holding the entire object
in memory before iteration.

When the yield statement is yit, the program suspends function execution and returns
the yielded value (return stops execution completely). When a function is suspended, 
the state of that function is saved. This includes any variable bindings local to the 
generator, the instruction pointer, the internal stack, and any exception handling.
"""

"""generator vs list

comparing them using sys.getsizeof() - the memory size of object
"""
names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

people = people_list(1000000)
sys.getsizeof(people) # 8448728 bytes

people1 = people_generator(1000000)
sys.getsizeof(people1) # 112 bytes

"""reading large files"""
# bad - f.read().split('\n') loads everything into memory at once
def csv_reader(file_name):
    with open(file_name, 'r') as f:
        result = f.read().split('\n')
        return result

# good - open the file loop though each line, yields each row instead of returning 
def csv_reader1(file_name):
    for row in open(file_name, 'r'):
        yield row

csv_gen = (row for row in open('src/generators/sample_data.csv')) # generator comprehension