import unittest
from school import *

class TestScool(unittest.TestCase):

    # Name is a string, no numbers are allowed in the string, and name should not be empty
    # Cpr format 'xxxxxx-xxxx' where x is numbers, and is a valid cpr number

    def test_if_stud_name_is_a_string(self):

        student = Student()
        self.assertRaises(TypeError, , 12)