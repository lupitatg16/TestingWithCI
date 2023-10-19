import unittest
import calculator  # Importa el módulo que deseas probar

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)  # Prueba que 2 + 3 sea igual a 5
        self.assertEqual(calculator.add(-1, 1), 0)  # Prueba que -1 + 1 sea igual a 0
        self.assertEqual(calculator.add(-1, -1), -2)  # Prueba que -1 + (-1) sea igual a -2
    
    def test_sub(self):
        self.assertEqual(calculator.subtract(2, 3), -1)  # Prueba que 2 + 3 sea igual a 5
        self.assertEqual(calculator.subtract(-1, 1), -2)  # Prueba que -1 + 1 sea igual a 0
        self.assertEqual(calculator.subtract(-1, -1), 0)  # Prueba que -1 + (-1) sea igual a -2

    def test_mul(self):
            self.assertEqual(calculator.multiply(2, 3), 6)  # Prueba que 2 + 3 sea igual a 5
            self.assertEqual(calculator.multiply(-1, 1), -1)  # Prueba que -1 + 1 sea igual a 0
            self.assertEqual(calculator.multiply(-1, -1), 1)  # Prueba que -1 + (-1) sea igual a -2

    def test_div(self):
            self.assertEqual(calculator.divide(4, 2), 2)  # Prueba que 2 + 3 sea igual a 5
            self.assertEqual(calculator.divide(-1, 1), -1) 
            self.assertEqual(calculator.divide(1, 0), "Error") 

if __name__ == '__main__':
    unittest.main()
