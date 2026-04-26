"""
Archivo principal de la aplicación web.

Este módulo configura Flask, define las rutas principales y conecta
la vista HTML con la lógica de la calculadora bitwise.
"""

from flask import Flask, render_template, request

from models.bitwise_calculator import BitwiseCalculator


app = Flask(__name__)
calculator = BitwiseCalculator()


def get_integer_from_form(field_name):
    """
    Obtiene un valor del formulario y lo convierte a entero.

    Args:
        field_name (str): Nombre del campo enviado desde el formulario.

    Returns:
        int: Valor convertido a número entero.

    Raises:
        ValueError: Si el campo está vacío o no es un número entero.
    """
    value = request.form.get(field_name, "").strip()

    if value == "":
        raise ValueError("Todos los campos necesarios deben estar llenos.")

    try:
        return int(value)
    except ValueError as error:
        raise ValueError("Ingrese solamente números enteros.") from error


def calculate_bitwise_operation(operation, first_number, second_number=None):
    """
    Ejecuta la operación bitwise seleccionada por el usuario.

    Args:
        operation (str): Operación seleccionada.
        first_number (int): Primer número entero.
        second_number (int | None): Segundo número entero o posiciones.

    Returns:
        int: Resultado de la operación bitwise.

    Raises:
        ValueError: Si la operación no existe.
    """
    if operation == "and":
        return calculator.and_operation(first_number, second_number)

    if operation == "or":
        return calculator.or_operation(first_number, second_number)

    if operation == "xor":
        return calculator.xor_operation(first_number, second_number)

    if operation == "not":
        bit_width = get_integer_from_form("bit_width")
        return calculator.not_operation(first_number, bit_width)

    if operation == "left_shift":
        return calculator.left_shift(first_number, second_number)

    if operation == "right_shift":
        return calculator.right_shift(first_number, second_number)

    raise ValueError("Operación no válida.")


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Renderiza la página principal y procesa las operaciones bitwise.

    Returns:
        str: Plantilla HTML renderizada.
    """
    result_decimal = None
    result_binary = None
    error_message = None

    form_data = {
        "first_number": "",
        "second_number": "",
        "operation": "and",
        "bit_width": "8"
    }

    if request.method == "POST":
        form_data["first_number"] = request.form.get("first_number", "")
        form_data["second_number"] = request.form.get("second_number", "")
        form_data["operation"] = request.form.get("operation", "and")
        form_data["bit_width"] = request.form.get("bit_width", "8")

        try:
            operation = form_data["operation"]
            first_number = get_integer_from_form("first_number")
            second_number = None

            if operation != "not":
                second_number = get_integer_from_form("second_number")

            result_decimal = calculate_bitwise_operation(
                operation,
                first_number,
                second_number
            )

            result_binary = calculator.to_binary(result_decimal)

        except (TypeError, ValueError) as error:
            error_message = str(error)

    return render_template(
        "index.html",
        result_decimal=result_decimal,
        result_binary=result_binary,
        error_message=error_message,
        form_data=form_data
    )


if __name__ == "__main__":
    app.run(debug=True)
