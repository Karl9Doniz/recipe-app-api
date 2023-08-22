"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Import the calc module"""

    def test_add_numbers(self):
        """Test the add method"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test the subtraction method"""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)