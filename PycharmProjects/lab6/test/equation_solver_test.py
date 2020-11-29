import unittest

from equations_solver import count_quadratic_equation, count_linear_equation, count_equation


class MyTestCase(unittest.TestCase):
    def test_quadratic_equation_no_solutions(self):
        self.assertRaises(ValueError, count_quadratic_equation, 1, 2, 3)  # no solutions

    def test_quadratic_equation_one_solution(self):
        self.assertAlmostEqual(count_quadratic_equation(2, 4, 2), -1)

    def test_quadratic_equation_two_solutions(self):
        x1, x2 = count_quadratic_equation(1, 4, 3)
        self.assertAlmostEqual(x1, -1.0)
        self.assertAlmostEqual(x2, -3.0)
        x1, x2 = count_quadratic_equation(1.5, 6.453, 3.99)
        self.assertAlmostEqual(x1, -0.7485731748144575)
        self.assertAlmostEqual(x2, -3.553426825185543)

    def test_linear_equation_ab_zero(self):
        self.assertRaises(ValueError, count_linear_equation, 0, 0)  # infinite number of solutions

    def test_linear_equation_a_zero(self):
        self.assertRaises(ValueError, count_linear_equation, 0, 3)  # contradictory equation

    def test_linear_equation_ab_nonzero(self):
        self.assertAlmostEqual(count_linear_equation(2, 3), -1.5)
        self.assertAlmostEqual(count_linear_equation(2.3, 32.1), -13.956521739130437)

    def test_count_equation(self):
        self.assertAlmostEqual(count_linear_equation(2, 3), count_equation(0, 2, 3))
        self.assertAlmostEqual(count_quadratic_equation(0.1, -4, 0.3), count_equation(0.1, -4, 0.3))


if __name__ == '__main__':
    unittest.main()
