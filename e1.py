"""
Create a class ​ Person​ with the attributes:
● name
● lastname
● age
● address.
Functionality:
● These attributes are mandatory to create an object from this class.
● The name and lastname should be private.
● Add a method to return the person’s fullname.
● Create some instances of this class as an example.
● Add a method to this class in order to return an instance of Person without the age.
● Add a variable to the class that allow us to know how many instances of Person has
been created.
● Create a class​ Employee ​ that inherits the behaviors of Person. Include the following
attributes:
○ employee code
○ salary per hour
○ start date
○ position
○ the department what they belong.
● Add some tests to validate this functionality.
"""

class Person(object):
    
    instances = 0
    
    def __init__(self, name, lastname, age, address):
        self._name = name
        self._lastname = lastname
        self.age = age
        self.address = address
        type(self).instances += 1

    def get_full_name(self):
        return f'{self._name} {self._lastname}'
    
    def without_age(self):
        pass

    def json_repr(self):
        return {
            'name': self._name,
            'lastname': self._lastname,
            'age': self.age,
            'address': self.address
        }

class Employee(Person):
    
    def __init__(self, name, lastname, age, address, code, salary, start_date, position, department):
        super().__init__(name, lastname, age, address)
        self.employee_code = code
        self.salary_per_hour = salary
        self.start_date = start_date
        self.position = position
        self.department = department

    def json_repr(self):
        json_repr = super().json_repr()
        added_repr = {
            'employee_code': self.employee_code,
            'salary_per_hour': self.salary_per_hour,
            'start_date': self.start_date,
            'position': self.position,
            'department': self.department
        }
        for key, value in added_repr.items():
            json_repr[key] = value
        return json_repr

if __name__ == '__main__':
    for i in ['holi', 'nya', 'miau']:
        m1 = Person(i, 'gatito', 12, 'miau')
        print(m1.get_full_name())
        print(m1.instances)