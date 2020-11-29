import unittest

from equations_finder import find_equation


class TestEquationFinder(unittest.TestCase):
    def test_find_equation_same_points(self):
        self.assertRaises(ValueError, find_equation, (0, 1), (0, 1))
        self.assertRaises(ValueError, find_equation, (0, -1.324), (0, -1.324))

    def test_find_equation_different_points(self):
        self.assertEqual(find_equation((1, 2), (3, 4)), "y=1.0x+1.0")
        self.assertEqual(find_equation((1, 5), (-1, 4)), "y=0.5x+4.5")
        self.assertEqual(find_equation((-1, 2.64), (3.4, -4.43)), "y=-1.6068181818181817x+1.0331818181818184")


if __name__ == '__main__':
    unittest.main()
