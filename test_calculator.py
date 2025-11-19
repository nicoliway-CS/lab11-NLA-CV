#https://github.com/nicoliway-CS/lab11-NLA-CV.git
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    #Camila Valdez
    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(-4,4),0)
        self.assertEqual(add(-6,-5),-11)
    #Camila Valdez
    def test_subtract(self):
        self.assertEqual(subtract(-2,-3), 1 )
        self.assertEqual(subtract(4,-6), 10)
        self.assertEqual(subtract(2,2), 0)

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(5,4), 20)
        self.assertEqual(mul(-1,8), -8)
        self.assertEqual(mul(-4,0),0)
        self.assertEqual(mul(-3,-2),6)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(10,10),1)
        self.assertAlmostEqual(div(3,10),3.333, places=3)
        self.assertEqual(div(-2,6),-3)

    #Camila Valdez
    def test_divide_by_zero(self): #
        with self.assertRaises(ZeroDivisionError):
            div(0,5)
            


    #     # c
    #
    #     all division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    def test_logarithm(self):
        self.assertEqual(logarithm(8, 2), 3)
        self.assertAlmostEqual(logarithm(100, 10), 2)
        self.assertAlmostEqual(logarithm(1, 5), 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(10, 1)

    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(0, 5)
        with self.assertRaises(ValueError):
            log(-5, 6)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3,5),5.83,places=2)
        self.assertAlmostEqual(hypotenuse(6,2),6.32,places=2)
        self.assertAlmostEqual(hypotenuse(-3,5),5.83,places=2)
        self.assertAlmostEqual(hypotenuse(0,9),9)



    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-5)

        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(100), 10)
        self.assertAlmostEqual(square_root(56),7.48,places=2)
        self.assertEqual(square_root(0),0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()