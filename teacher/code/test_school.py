import unittest
from school import *

class TestSchool(unittest.TestCase):

    def test_numbers_in_create_student(self):
        # Name is a string of letters, no numbers are allowed
        # Cpr format 'xxxxxx-xxxx' where x is numbers
        self.assertRaises(ValueError, Student, 'Claus 123', 221070-1919)

    def test_type_create_student(self):
        self.assertRaises(TypeError, Student, 1, 1)

    def test_if_empty_name_create_student(self):
        self.assertRaises(ValueError, Student, None, None)

