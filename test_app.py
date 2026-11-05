import unittest
from app import add
from number_tools import is_even


class TestAdd(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even(4))

    def test_odd_number(self):
        self.assertFalse(is_even(5))


if __name__ == "__main__":
    unittest.main()
