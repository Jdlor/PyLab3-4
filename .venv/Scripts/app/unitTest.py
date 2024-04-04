import unittest
from math import sqrt
from run import UravnSolver
class TestCalculator(unittest.TestCase):
  def test_one(self):
    self.assertEqual(UravnSolver.uravn(10,1,1), 'дискриминант меньше нуля, корней нет')

  def test_two(self):
    self.assertEqual(UravnSolver.uravn(2, 4, 2), '1 корень, х= -1.0')

  def test_three(self):
    self.assertEqual(UravnSolver.uravn(2, 5, 2), '2 корня, х1 = -0.5 x2 = -2.0')

  def test_four(self):
    self.assertEqual(UravnSolver.uravn('', '', ''), 'все поля должны быть заполнены')

  def test_five(self):
    self.assertEqual(UravnSolver.uravn('', 1, 8), 'все поля должны быть заполнены')

  def test_six(self):
    self.assertEqual(UravnSolver.uravn('x', 'x', 'x'), 'введёные данные должны быть числами (дробные числа следует разделять точкой)')

  def test_seven(self):
    self.assertEqual(UravnSolver.uravn(2.5, 3, 2.25), 'дискриминант меньше нуля, корней нет')
if __name__ == "__main__":
  unittest.main()