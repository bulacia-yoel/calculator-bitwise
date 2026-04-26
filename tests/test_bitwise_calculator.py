"""
Pruebas unitarias para la clase BitwiseCalculator.

Este módulo verifica que las operaciones bitwise funcionen correctamente.
"""

import unittest

from models.bitwise_calculator import BitwiseCalculator


class TestBitwiseCalculator(unittest.TestCase):
    """
    Clase de pruebas para las operaciones bitwise.
    """

    def setUp(self):
        """
        Inicializa una calculadora antes de cada prueba.
        """
        self.calculator = BitwiseCalculator()

    def test_and_operation(self):
        """
        Verifica la operación AND.
        """
        result = self.calculator.and_operation(5, 3)
        self.assertEqual(result, 1)

    def test_or_operation(self):
        """
        Verifica la operación OR.
        """
        result = self.calculator.or_operation(5, 3)
        self.assertEqual(result, 7)

    def test_xor_operation(self):
        """
        Verifica la operación XOR.
        """
        result = self.calculator.xor_operation(5, 3)
        self.assertEqual(result, 6)

    def test_not_operation(self):
        """
        Verifica la operación NOT usando 4 bits.
        """
        result = self.calculator.not_operation(5, 4)
        self.assertEqual(result, 10)

    def test_left_shift(self):
        """
        Verifica el desplazamiento hacia la izquierda.
        """
        result = self.calculator.left_shift(5, 1)
        self.assertEqual(result, 10)

    def test_right_shift(self):
        """
        Verifica el desplazamiento hacia la derecha.
        """
        result = self.calculator.right_shift(5, 1)
        self.assertEqual(result, 2)

    def test_to_binary(self):
        """
        Verifica la conversión a binario.
        """
        result = self.calculator.to_binary(5)
        self.assertEqual(result, "0b101")


if __name__ == "__main__":
    unittest.main()
