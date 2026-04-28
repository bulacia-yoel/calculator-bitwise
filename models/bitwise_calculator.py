"""
Módulo de lógica para la calculadora bitwise.

Este archivo contiene la clase BitwiseCalculator, encargada de realizar
operaciones bitwise sobre números enteros.
"""


class BitwiseCalculator:
    """
    Clase encargada de realizar operaciones bitwise.

    Esta clase contiene métodos para operaciones AND, OR, XOR, NOT,
    desplazamiento a la izquierda y desplazamiento a la derecha.
    """

    @staticmethod
    def validate_integer(value):
        """
        Valida que un valor sea un número entero.

        Args:
            value (int): Valor que será validado.

        Raises:
            TypeError: Si el valor no es un número entero.
        """
        if not isinstance(value, int):
            raise TypeError("El valor debe ser un número entero.")

    @staticmethod
    def validate_shift_positions(positions):
        """
        Valida que las posiciones de desplazamiento sean correctas.

        Args:
            positions (int): Cantidad de posiciones a desplazar.

        Raises:
            TypeError: Si positions no es un número entero.
            ValueError: Si positions es negativo.
        """
        if not isinstance(positions, int):
            raise TypeError("Las posiciones deben ser un número entero.")

        if positions < 0:
            raise ValueError("Las posiciones no pueden ser negativas.")

    def and_operation(self, first_number, second_number):
        """
        Realiza la operación bitwise AND entre dos números enteros.

        Args:
            first_number (int): Primer número entero.
            second_number (int): Segundo número entero.

        Returns:
            int: Resultado de first_number AND second_number.
        """
        self.validate_integer(first_number)
        self.validate_integer(second_number)

        return first_number & second_number

    def or_operation(self, first_number, second_number):
        """
        Realiza la operación bitwise OR entre dos números enteros.

        Args:
            first_number (int): Primer número entero.
            second_number (int): Segundo número entero.

        Returns:
            int: Resultado de first_number OR second_number.
        """
        self.validate_integer(first_number)
        self.validate_integer(second_number)

        return first_number | second_number

    def xor_operation(self, first_number, second_number):
        """
        Realiza la operación bitwise XOR entre dos números enteros.

        Args:
            first_number (int): Primer número entero.
            second_number (int): Segundo número entero.

        Returns:
            int: Resultado de first_number XOR second_number.
        """
        self.validate_integer(first_number)
        self.validate_integer(second_number)

        return first_number ^ second_number

    def not_operation(self, number, bit_width=8):
        """
        Realiza la operación bitwise NOT sobre un número entero.

        Se usa una cantidad fija de bits para evitar resultados negativos
        como ocurre normalmente en Python con el operador ~.

        Args:
            number (int): Número entero.
            bit_width (int): Cantidad de bits que se tomarán en cuenta.

        Returns:
            int: Resultado de la operación NOT.
        """
        self.validate_integer(number)
        self.validate_integer(bit_width)

        if bit_width <= 0:
            raise ValueError("La cantidad de bits debe ser mayor que cero.")

        mask = (1 << bit_width) - 1

        return ~number & mask

    def left_shift(self, number, positions):
        """
        Desplaza los bits de un número hacia la izquierda.

        Args:
            number (int): Número entero.
            positions (int): Cantidad de posiciones a desplazar.

        Returns:
            int: Resultado del desplazamiento hacia la izquierda.
        """
        self.validate_integer(number)
        self.validate_shift_positions(positions)

        return number << positions

    def right_shift(self, number, positions):
        """
        Desplaza los bits de un número hacia la derecha.

        Args:
            number (int): Número entero.
            positions (int): Cantidad de posiciones a desplazar.

        Returns:
            int: Resultado del desplazamiento hacia la derecha.
        """
        self.validate_integer(number)
        self.validate_shift_positions(positions)

        return number >> positions

    def to_binary(self, number):
        """
        Convierte un número entero a representación binaria.

        Args:
            number (int): Número entero.

        Returns:
            str: Número representado en binario.
        """
        self.validate_integer(number)

        return format(number, "b")
