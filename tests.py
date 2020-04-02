import unittest
from gc import collect
from copy import deepcopy
from e1 import Person, Employee
from e2 import get_lower_paid_employees, load_unique_records
from e3 import check_types


class PersonTestCase(unittest.TestCase):
    """Test functionalities of e1 script
    """

    def setUp(self):
        self.exp_person = Person('john','carpenter',23,'32 Av los robles, pasadena')

    def tearDown(self):
        self.exp_person = None
        collect()

    def test_without_age(self):
        new_person = self.exp_person.without_age()
        self.assertTrue(hasattr(new_person, 'age'))

    def test_full_name(self):
        self.assertEqual(self.exp_person.get_full_name(), 'john carpenter')

    def test_instance_number(self):
        instances_created = deepcopy(self.exp_person.instances)
        person_list = []
        for lastname in ['wick', 'constantine']:
            person_list.append(Person('john', lastname, 24,'arkam asylum, gotham'))
        self.assertEqual(instances_created + 2, self.exp_person.instances)


class loadFilesTestCase(unittest.TestCase):
    
    def setUp(self):
        self.filename = 'test_empleados.txt'

    def tearDown(self):
        pass

    def test_load_unique_records(self):
        data = load_unique_records(self.filename)
        self.assertEqual(len(data), 8)

    def test_get_lower_paid_employees(self):
        data = get_lower_paid_employees(self.filename)
        self.assertEqual(len(data), 2)
        lower_rate = data[1]['salary']
        self.assertEqual(lower_rate, 100)


@check_types(int, str, list)
def call_me_many_times(times, name, appointments):
    for attempt in range(times):
        for appointment in appointments:
            print(f'{attempt}) {name} its time to {appointment}')
    return True


class check_typesTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = 'test_empleados.txt'

    def tearDown(self):
        pass

    def test_ok_validation(self):
        self.assertTrue(call_me_many_times(10, 'john', ['cook', 'paint', 'work']))

    def test_error_validation(self):
        try:
            state = call_me_many_times('10', 'john', ['cook', 'paint', 'work'])
        except Exception as err:
            state = False
        finally:
            self.assertFalse(state)


if __name__ == '__main__':
    unittest.main()

