import logging

"""Logging in Python

# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
"""

"""Basic logger

logging.basicConfig(filename='src/logging/test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
"""

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create file handler and set level to debug
file_handler = logging.FileHandler('src/logging/test.log')
file_handler.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('[%(asctime)s] %(name)s %(levelname)s (%(funcName)s) %(message)s')

# add formatter to file handler
logger.addHandler(file_handler)

# add file handler to logger
file_handler.setFormatter(formatter)

class Employee:
    emp_count = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Employee.emp_count += 1
        logger.debug(f"Employee number {Employee.emp_count} has been created.")

emp_1 = Employee('Bob', 'Jane')
emp_3 = Employee('John', 'Smith')
emp_2 = Employee('Luke', 'Skywalker')