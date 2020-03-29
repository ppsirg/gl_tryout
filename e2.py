"""
Write a function to read a file with employees details.
This is a file separated by ​ “;”​ , named empleados.txt. which contains the names of the
columns in the first line like this:

employee_code
name
lastname
address
age
start_date
salary
position
department.

This file could contain repeated records. You’ll need to think of a way to get unique
employees or unique records.
Functionality:
● Get the employees with the lower rate per hour (lower salary). You can use
comprehensions to solve it.
● Add some tests to validate this functionality.
"""

import csv

def load_unique_records(filename):
    with open(filename, 'r') as file_cursor:
        reader = [tuple(a.items()) for a in csv.DictReader(file_cursor, delimiter=';')]
        unique_records = set(reader)
        return unique_records


def get_lower_paid_employees(filename):
    data = load_unique_records(filename)
    dict_data = [dict(a) for a in data]
    lower_rate = min([a['salary'] for a in dict_data])
    return [a for a in dict_data if a['salary'] == lower_rate]


if __name__ == '__main__':
    data = load_unique_records('empleados.txt')
    print(len(data), data)