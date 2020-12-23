import logging

"""Logging in Python

# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
"""

logging.basicConfig(level=logging.DEBUG, filename='src/logging/test.log', format='%(asctime)s:%(levelname)s:%(message)s')

class Employee:
    emp_count = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Employee.emp_count += 1
        logging.debug(f"Employee number {Employee.emp_count} has been created.")

emp_1 = Employee('Bob', 'Jane')
emp_3 = Employee('John', 'Smith')
emp_2 = Employee('Luke', 'Skywalker')