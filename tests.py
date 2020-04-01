from unittest import TestCase
from gc import collect
from copy import deepcopy
from e1 import Person, Employee
from e2 import get_lower_paid_employees, load_unique_records


class PersonTestCase(TestCase):
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


class loadFilesTestCase(TestCase):
    
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

