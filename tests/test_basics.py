"""Regression tests for the initial stabilization pass."""
import unittest
from basics import arithmetic, utilities, fractions, roots

class TestBasics(unittest.TestCase):
    def test_arithmetic(self):
        self.assertEqual(arithmetic.add(2, 3), 5)
        self.assertEqual(arithmetic.average(2, 4, 6), 4)

    def test_utilities(self):
        self.assertEqual(utilities.mean(2, 4, 6), 4)
        self.assertEqual(utilities.distance(-2, 3), 5)
        self.assertEqual(utilities.modular_distance(1, 19, 10), 2)
        self.assertEqual(utilities.nearest_multiple(-7, 5), -5)
        self.assertEqual(utilities.next_multiple(10, 5), 15)
        self.assertEqual(utilities.previous_multiple(10, 5), 5)
        self.assertEqual(utilities.next_multiple(-11, -5), -10)
        with self.assertRaises(ValueError):
            utilities.cyclic_wrap(3, 4, 4)

    def test_fractions(self):
        self.assertEqual(fractions.simplify_fraction(6, -8), (-3, 4))
        self.assertEqual(fractions.compare_fractions(1, -2, 1, 3), -1)
        self.assertEqual(fractions.compare_fractions(1, -2, -1, 2), 0)

    def test_exact_roots(self):
        huge = 12345678901234567890123456789
        self.assertTrue(roots.is_perfect_square(huge * huge))
        self.assertFalse(roots.is_perfect_square(huge * huge + 1))
        self.assertTrue(roots.is_perfect_cube(-huge ** 3))
        self.assertTrue(roots.is_perfect_power(-243, 5))
        self.assertFalse(roots.is_perfect_power(-256, 4))

if __name__ == "__main__":
    unittest.main()
