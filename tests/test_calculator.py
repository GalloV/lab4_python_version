import unittest
import sys
import os
from calculator import Calculator


# Add src directory to path so we can import calculator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))



class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add(self):
        """Test addition operation."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2.5, 2.5), 5.0)

    def test_subtract(self):
        """Test subtraction operation."""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(5, 5), 0)

    def test_multiply(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(6, 7), 42)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-3, 4), -12)

    def test_divide(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(20, 4), 5)
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)

    def test_divide_by_zero(self):
        """Test that dividing by zero raises an error."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_power(self):
        """Test power operation."""
        self.assertEqual(self.calc.power(2, 8), 256)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(10, 0), 1)


if __name__ == "__main__":
    
    unittest.main()
