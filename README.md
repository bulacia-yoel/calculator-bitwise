<div align="center">

# 🧮 Calculadora Bitwise

### Aplicación web minimalista para realizar operaciones bitwise con Python y Flask.

![Python](https://img.shields.io/badge/Python-3.x-222222?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-222222?style=for-the-badge&logo=flask)
![HTML](https://img.shields.io/badge/HTML-Frontend-222222?style=for-the-badge&logo=html5)
![CSS](https://img.shields.io/badge/CSS-Styles-222222?style=for-the-badge&logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-Interaction-222222?style=for-the-badge&logo=javascript)

</div>

---

## 📌 Descripción

**Calculadora Bitwise** es una aplicación web desarrollada con **Python**, **Flask**, **HTML**, **CSS** y **JavaScript**.

El objetivo del proyecto es permitir al usuario realizar operaciones bitwise sobre números enteros mediante una interfaz web simple, ordenada, minimalista y funcional.

Este proyecto separa correctamente la lógica del programa, la vista del usuario y los archivos estáticos, siguiendo una estructura limpia y fácil de mantener.

---

## ⚙️ Operaciones disponibles

La calculadora permite realizar las siguientes operaciones:

| Operación | Descripción |
|---|---|
| `AND` | Compara dos números bit a bit y devuelve `1` solo si ambos bits son `1`. |
| `OR` | Compara dos números bit a bit y devuelve `1` si al menos uno de los bits es `1`. |
| `XOR` | Devuelve `1` cuando los bits comparados son diferentes. |
| `NOT` | Invierte los bits de un número usando una cantidad fija de bits. |
| `Left Shift` | Desplaza los bits hacia la izquierda. |
| `Right Shift` | Desplaza los bits hacia la derecha. |

---

## 🛠️ Tecnologías utilizadas

### Backend

- Python
- Flask

### Frontend

- HTML
- CSS
- JavaScript

### Pruebas

- unittest

---

## 📁 Estructura del proyecto

```text
calculator-bitwise/
│
├── models/
│   ├── __init__.py
│   └── bitwise_calculator.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── styles.css
│   │
│   └── js/
│       └── main.js
│
├── tests/
│   └── test_bitwise_calculator.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🧩 Función de cada archivo

### `app.py`

Archivo principal del proyecto.

Se encarga de:

- Crear la aplicación Flask.
- Levantar el servidor.
- Definir la ruta principal.
- Recibir los datos enviados desde el formulario.
- Validar los datos ingresados.
- Conectar la vista HTML con la lógica de Python.
- Enviar el resultado nuevamente al navegador.

---

### `models/bitwise_calculator.py`

Contiene la clase principal del proyecto:

```python
BitwiseCalculator
```

Esta clase se encarga de realizar todas las operaciones bitwise.

Incluye métodos para:

- `and_operation()`
- `or_operation()`
- `xor_operation()`
- `not_operation()`
- `left_shift()`
- `right_shift()`
- `to_binary()`

---

### `templates/index.html`

Contiene la interfaz principal de la calculadora.

Desde este archivo el usuario puede:

- Ingresar el primer número.
- Seleccionar la operación.
- Ingresar el segundo número o cantidad de posiciones.
- Elegir la cantidad de bits para la operación `NOT`.
- Visualizar el resultado en decimal y binario.
- Ver mensajes de error si los datos son incorrectos.

---

### `static/css/styles.css`

Archivo encargado del diseño visual de la aplicación.

Incluye:

- Diseño minimalista.
- Colores neutros.
- Tarjeta central.
- Inputs estilizados.
- Botón principal.
- Tarjeta de resultado.
- Tarjeta de error.
- Diseño responsive para celulares.

---

### `static/js/main.js`

Archivo encargado de mejorar la interacción del formulario.

Permite:

- Ocultar el segundo número cuando se selecciona `NOT`.
- Mostrar el campo de cantidad de bits para `NOT`.
- Cambiar el texto del segundo campo cuando se usan desplazamientos.
- Mejorar la experiencia del usuario sin recargar elementos innecesarios.

---

### `tests/test_bitwise_calculator.py`

Archivo donde se realizan pruebas unitarias de la clase `BitwiseCalculator`.

Sirve para comprobar que las operaciones principales funcionan correctamente.

---

### `requirements.txt`

Archivo donde se guardan las dependencias necesarias del proyecto.

Actualmente contiene:

```text
Flask
```

---

## 🚀 Instalación y ejecución

### 1. Entrar a la carpeta del proyecto

```bash
cd calculator-bitwise
```

---

## 🐍 Crear entorno virtual

Se recomienda usar un entorno virtual para mantener las dependencias ordenadas.

### En Linux

```bash
python3 -m venv env
```

Activar entorno virtual:

```bash
source env/bin/activate
```

---

### En Windows

```bash
python -m venv env
```

Activar en CMD:

```cmd
env\Scripts\activate
```

Activar en PowerShell:

```powershell
env\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación, ejecutar:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Luego volver a activar:

```powershell
env\Scripts\Activate.ps1
```

---

## 📦 Instalar dependencias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecutar la aplicación

Desde la raíz del proyecto:

```bash
python app.py
```

Luego abrir en el navegador:

```text
http://127.0.0.1:5000
```

---

## 🧪 Ejecutar pruebas unitarias

Desde la raíz del proyecto:

```bash
python -m unittest discover tests
```

Si todo está correcto, debería aparecer algo parecido a:

```text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

Esto significa que las operaciones principales fueron probadas correctamente.

---

## 🧠 Ejemplos de uso

### Operación AND

```text
Primer número: 5
Operación: AND
Segundo número: 3
```

Resultado:

```text
Decimal: 1
Binario: 0b1
```

Explicación:

```text
5 = 101
3 = 011

101 AND 011 = 001
```

---

### Operación OR

```text
Primer número: 5
Operación: OR
Segundo número: 3
```

Resultado:

```text
Decimal: 7
Binario: 0b111
```

Explicación:

```text
5 = 101
3 = 011

101 OR 011 = 111
```

---

### Operación XOR

```text
Primer número: 5
Operación: XOR
Segundo número: 3
```

Resultado:

```text
Decimal: 6
Binario: 0b110
```

Explicación:

```text
5 = 101
3 = 011

101 XOR 011 = 110
```

---

### Operación NOT

```text
Primer número: 5
Operación: NOT
Cantidad de bits: 4
```

Resultado:

```text
Decimal: 10
Binario: 0b1010
```

Explicación:

```text
5 en 4 bits = 0101

NOT 0101 = 1010
```

---

### Desplazamiento a la izquierda

```text
Primer número: 5
Operación: Desplazamiento izquierda
Cantidad de posiciones: 1
```

Resultado:

```text
Decimal: 10
Binario: 0b1010
```

Explicación:

```text
5 = 101

101 << 1 = 1010
```

---

### Desplazamiento a la derecha

```text
Primer número: 5
Operación: Desplazamiento derecha
Cantidad de posiciones: 1
```

Resultado:

```text
Decimal: 2
Binario: 0b10
```

Explicación:

```text
5 = 101

101 >> 1 = 10
```

---

## ✅ Validaciones implementadas

La aplicación valida que:

- Los campos necesarios no estén vacíos.
- Los valores ingresados sean números enteros.
- La operación seleccionada sea válida.
- La cantidad de bits para `NOT` sea mayor que cero.
- Las posiciones de desplazamiento no sean negativas.
- Los errores se muestren de forma clara al usuario.

---

## 🔄 Flujo general del programa

```text
Usuario ingresa datos en el formulario
                │
                ▼
Flask recibe los datos en app.py
                │
                ▼
app.py valida los datos
                │
                ▼
Se llama a la clase BitwiseCalculator
                │
                ▼
Se realiza la operación bitwise
                │
                ▼
Flask envía el resultado al HTML
                │
                ▼
El usuario visualiza el resultado
```

---

## 🧼 Buenas prácticas aplicadas

El proyecto busca seguir buenas prácticas de programación en Python y organización web.

Se aplican criterios como:

- Código separado por responsabilidades.
- Uso de clases para la lógica principal.
- Uso de funciones auxiliares.
- Nombres descriptivos.
- Comentarios claros.
- Docstrings en clases y funciones.
- Validación de datos.
- Estructura ordenada.
- Diseño limpio y minimalista.
- Pruebas unitarias para verificar la lógica.

---

## 🗃️ Mejora futura: Base de datos

Como mejora opcional, se puede agregar una base de datos para guardar el historial de operaciones realizadas.

Una posible estructura futura sería:

```text
calculator-bitwise/
│
├── database/
│   ├── connection.py
│   └── calculator.db
```

La base de datos podría guardar información como:

```text
Operación: AND
Primer número: 5
Segundo número: 3
Resultado decimal: 1
Resultado binario: 0b1
Fecha de creación: 2026-04-26
```

Para este proyecto, una buena opción sería usar **SQLite**, ya que es simple, ligera y adecuada para proyectos académicos pequeños.

---

## 📊 Estado actual del proyecto

| Fase | Estado |
|---|---|
| Estructura base | ✅ Completado |
| Servidor Flask | ✅ Completado |
| Lógica bitwise | ✅ Completado |
| Conexión Flask + lógica | ✅ Completado |
| Interfaz visual | ✅ Completado |
| Validaciones básicas | ✅ Completado |
| Pruebas unitarias | ✅ Completado |
| Documentación README | ✅ Completado |
| Base de datos | ⏳ Opcional |

---

## 👨‍💻 Autor

**Estudiate: Yoel Bulacia**
[Ver mis proyectos](https://github.com/bulacia-yoel/)

---

<div align="center">

### 🧮 Calculadora Bitwise
Código ordenado, interfaz minimalista y lógica separada por clases.

</div>
