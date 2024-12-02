import unittest
from main import pyramid_number

class TestPyramidNumber(unittest.TestCase):
    
    def test_positive_number(self):
        self.assertEqual(pyramid_number(1), 1)
        self.assertEqual(pyramid_number(2), 4)
        self.assertEqual(pyramid_number(5), 35)

    def test_zero_input(self):
        with self.assertRaises(ValueError):
            pyramid_number(0)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            pyramid_number(-3)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            pyramid_number("5")
    
if __name__ == "__main__":
    unittest.main()