/**
 * Archivo principal de interacción del cliente.
 *
 * Este script controla el comportamiento visual del formulario
 * según la operación bitwise seleccionada.
 */

document.addEventListener("DOMContentLoaded", function () {
    const operationSelect = document.getElementById("operation");
    const secondNumberGroup = document.getElementById("second-number-group");
    const secondNumberInput = document.getElementById("second_number");
    const secondNumberLabel = document.getElementById("second-number-label");
    const secondNumberHelp = document.getElementById("second-number-help");
    const bitWidthGroup = document.getElementById("bit-width-group");

    /**
     * Actualiza los campos visibles según la operación seleccionada.
     *
     * Para NOT no se necesita segundo número, pero sí cantidad de bits.
     * Para desplazamientos, el segundo campo representa posiciones.
     */
    function updateFormByOperation() {
        const selectedOperation = operationSelect.value;

        if (selectedOperation === "not") {
            secondNumberInput.value = "";
            secondNumberInput.disabled = true;
            secondNumberGroup.classList.add("hidden");
            bitWidthGroup.classList.remove("hidden");
            return;
        }

        secondNumberInput.disabled = false;
        secondNumberGroup.classList.remove("hidden");
        bitWidthGroup.classList.add("hidden");

        if (
            selectedOperation === "left_shift" ||
            selectedOperation === "right_shift"
        ) {
            secondNumberLabel.textContent = "Cantidad de posiciones";
            secondNumberInput.placeholder = "Ejemplo: 2";
            secondNumberHelp.textContent =
                "Indica cuántas posiciones se desplazarán los bits.";
        } else {
            secondNumberLabel.textContent = "Segundo número";
            secondNumberInput.placeholder = "Ejemplo: 3";
            secondNumberHelp.textContent =
                "Necesario para AND, OR y XOR.";
        }
    }

    operationSelect.addEventListener("change", updateFormByOperation);
    updateFormByOperation();
});
