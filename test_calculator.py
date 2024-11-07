import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:


    #add
    def test_add(self):
        self.assertEqual(self.calc.add(10, 1420), 1430)

    def test_add(self):
        self.assertEqual(self.calc.add(0, 450), 450)

    #substract()
    def test_substract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(5, 5), 0)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    #multiply
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(6, 2), 12)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(6, -2), -12)




    #divide
    def test_divide(self):
        self.assertEqual(self.calc.divide(20, 4), 5)

    def test_divide(self):
       self.assertEqual(self.calc.divide(200, 2), 100)
       self.assertEqual(self.calc.divide(3, -3), -1)

    

    #modulo
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(50, 6), 2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(44, 4), 0)



    

if __name__ == '__main__':
    unittest.main()