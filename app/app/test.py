"""
Sample tests

"""

from django.test import SimpleTestCase # noqa

from app import calc


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)
# noqa      

    def test_subract_numbers(self):
        res = calc.subtract(15, 10)
        self.assertEqual(res, 5)
