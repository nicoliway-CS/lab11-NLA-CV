import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

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

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
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