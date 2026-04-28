"""
Funciones auxiliares para trabajar con formularios.

Este módulo contiene validaciones y valores por defecto usados
en los formularios de la aplicación.
"""


def get_default_form_data():
    """
    Devuelve los valores por defecto del formulario.

    Returns:
        dict: Datos iniciales del formulario.
    """
    return {
        "first_number": "",
        "second_number": "",
        "operation": "and",
        "bit_width": "8"
    }


def get_integer_from_form(form, field_name):
    """
    Obtiene un valor del formulario y lo convierte a entero.

    Args:
        form: Datos enviados desde el formulario.
        field_name (str): Nombre del campo enviado desde el formulario.

    Returns:
        int: Valor convertido a número entero.

    Raises:
        ValueError: Si el campo está vacío o no es un número entero.
    """
    value = form.get(field_name, "").strip()

    if value == "":
        raise ValueError("Todos los campos necesarios deben estar llenos.")

    try:
        return int(value)
    except ValueError as error:
        raise ValueError("Ingrese solamente números enteros.") from error
