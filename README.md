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

Permite realizar operaciones bitwise sobre números enteros mediante una interfaz web simple, ordenada y funcional.

El proyecto está organizado por responsabilidades, separando la lógica, el control de rutas, la validación de datos y la vista del usuario.

---

## ⚙️ Operaciones disponibles

La calculadora permite realizar las siguientes operaciones:

| Operación | Descripción |
|---|---|
| `AND` | Compara dos números bit a bit y devuelve `1` solo si ambos bits son `1`. |
| `OR` | Devuelve `1` si al menos uno de los bits es `1`. |
| `XOR` | Devuelve `1` cuando los bits son diferentes. |
| `NOT` | Invierte los bits usando una cantidad fija de bits. |
| `<<` | Desplaza bits a la izquierda. |
| `>>` | Desplaza bits a la derecha. |

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
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── __init__.py
│   └── bitwise_calculator.py
│
├── controllers/
│   ├── __init__.py
│   ├── main_routes.py
│   ├── bitwise_service.py
│   └── form_helpers.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── main.js
│
└── tests/
    └── test_bitwise_calculator.py
