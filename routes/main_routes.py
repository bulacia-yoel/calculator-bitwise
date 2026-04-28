"""
Rutas principales de la aplicación web.

Este módulo contiene la ruta principal que muestra el formulario
y procesa las operaciones bitwise enviadas por el usuario.
"""

from flask import Blueprint, render_template, request

from models.bitwise_calculator import BitwiseCalculator
from services.bitwise_service import calculate_bitwise_operation
from utils.form_helpers import get_integer_from_form, get_default_form_data


main_routes = Blueprint("main_routes", __name__)

calculator = BitwiseCalculator()


@main_routes.route("/", methods=["GET", "POST"])
def index():
    """
    Renderiza la página principal y procesa las operaciones bitwise.

    Returns:
        str: Plantilla HTML renderizada.
    """
    result_decimal = None
    result_binary = None
    error_message = None

    form_data = get_default_form_data()

    if request.method == "POST":
        form_data["first_number"] = request.form.get("first_number", "")
        form_data["second_number"] = request.form.get("second_number", "")
        form_data["operation"] = request.form.get("operation", "and")
        form_data["bit_width"] = request.form.get("bit_width", "8")

        try:
            operation = form_data["operation"]
            first_number = get_integer_from_form(request.form, "first_number")
            second_number = None
            bit_width = None

            if operation != "not":
                second_number = get_integer_from_form(request.form, "second_number")
            else:
                bit_width = get_integer_from_form(request.form, "bit_width")

            result_decimal = calculate_bitwise_operation(
                calculator,
                operation,
                first_number,
                second_number,
                bit_width
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
