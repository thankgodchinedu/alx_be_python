import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    # --- Addition tests ---
    def test_addition_with_integers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_addition_with_floats_and_large_numbers(self):
        self.assertAlmostEqual(self.calc.add(2.5, 1.25), 3.75)
        self.assertEqual(self.calc.add(10**9, 1), 10**9 + 1)

    # --- Subtraction tests ---
    def test_subtraction_basic(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)  # negative result

    def test_subtraction_with_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    # --- Multiplication tests ---
    def test_multiplication_basic(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 12345), 0)

    def test_multiplication_with_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)

    # --- Division tests ---
    def test_division_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertAlmostEqual(self.calc.divide(1, 3), 1 / 3)

    def test_division_by_zero_returns_none(self):
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))  # 0/0 should also return None per implementation

    def test_division_with_negative_and_float(self):
        self.assertAlmostEqual(self.calc.divide(-10, 2), -5)
        self.assertAlmostEqual(self.calc.divide(5.5, 2), 2.75)

    # sanity check: chaining operations (optional)
    def test_chained_operations(self):
        # (2 + 3) * (10 - 4) / 5 = 5 * 6 / 5 = 6.0
        result = self.calc.divide(
            self.calc.multiply(self.calc.add(2, 3), self.calc.subtract(10, 4)),
            5,
        )
        self.assertAlmostEqual(result, 6.0)

if __name__ == "__main__":
    unittest.main()