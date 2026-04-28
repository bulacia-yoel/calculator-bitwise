"""
Servicio para ejecutar operaciones bitwise.

Este módulo conecta la operación seleccionada por el usuario
con los métodos de la calculadora bitwise.
"""


def calculate_bitwise_operation(
    calculator,
    operation,
    first_number,
    second_number=None,
    bit_width=None
):
    """
    Ejecuta la operación bitwise seleccionada por el usuario.

    Args:
        calculator (BitwiseCalculator): Instancia de la calculadora bitwise.
        operation (str): Operación seleccionada.
        first_number (int): Primer número entero.
        second_number (int | None): Segundo número entero o posiciones.
        bit_width (int | None): Cantidad de bits para la operación NOT.

    Returns:
        int: Resultado de la operación bitwise.

    Raises:
        ValueError: Si la operación no existe o faltan datos necesarios.
    """
    if operation == "and":
        return calculator.and_operation(first_number, second_number)

    if operation == "or":
        return calculator.or_operation(first_number, second_number)

    if operation == "xor":
        return calculator.xor_operation(first_number, second_number)

    if operation == "not":
        if bit_width is None:
            raise ValueError("Debe ingresar la cantidad de bits.")

        return calculator.not_operation(first_number, bit_width)

    if operation == "left_shift":
        return calculator.left_shift(first_number, second_number)

    if operation == "right_shift":
        return calculator.right_shift(first_number, second_number)

    raise ValueError("Operación no válida.")
