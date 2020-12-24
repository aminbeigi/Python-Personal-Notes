import random

"""Generators

We can create generator expressions without buidling and holding the entire object
in memory before iteration.
"""

"""generator instead of list"""
names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

people = people_generator(1000000)

"""reading large files"""
# bad - f.read().split('\n') loads everything into memory at once
def csv_reader(file_name):
    with open(file_name, 'r') as f:
        result = f.read().split('\n')
        return result

# good - open the file loop though each line, yields each row instead of returning 
def csv_reader2(file_name):
    for row in open(file_name, "r"):
        yield row

csv_gen = (row for row in open('src/generators/sample_data.csv')) # generator comprehension
