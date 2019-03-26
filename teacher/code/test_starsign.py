import unittest
from starsign import starsign

class TestStarsign(unittest.TestCase):

    def test_capricorn(self):
        self.assertEqual(starsign(1, 1), 'Capricorn' )


