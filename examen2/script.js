function esEntero(cadena) {
    if (!cadena) return false;
    for (let c of cadena) {
        if (c < '0' || c > '9') return false;
    }
    return true;
}

function esDecimal(cadena) {
    return cadena.includes('.');
}

function esTexto(cadena) {
    const letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚñÑ ";
    for (let c of cadena) {
        if (!letras.includes(c)) return false;
    }
    return true;
}

function convertirAEntero(cadena) {
    let numero = 0;
    for (let c of cadena) {
        numero = numero * 10 + (c.charCodeAt(0) - '0'.charCodeAt(0));
    }
    return numero;
}

function validarEntrada() {
    const entradaInput = document.getElementById('entrada');
    const entrada = entradaInput.value.trim();
    const resultado = document.getElementById('resultado');

    if (entrada.toLowerCase() === "salir") {
        resultado.textContent = "¡Programa terminado!";
        resultado.style.color = "green";
        entradaInput.disabled = true;
        return;
    }

    if (entrada === "") {
        resultado.textContent = "Entrada vacía";
        resultado.style.color = "orange";
        return;
    }

    if (esDecimal(entrada)) {
        resultado.textContent = "No se permiten decimales. Intenta de nuevo.";
        resultado.style.color = "blue";
        entradaInput.value = "";
        return;
    }

    if (esTexto(entrada)) {
        resultado.textContent = "No se permite texto. Intenta de nuevo.";
        resultado.style.color = "purple";
        entradaInput.value = "";
        return;
    }

    if (esEntero(entrada)) {
        const numero = convertirAEntero(entrada);
        resultado.textContent = `${numero} es un número entero muy bien!`;
        resultado.style.color = "green";
    } else {
        resultado.textContent = "Entrada no válida. Intenta con un número entero.";
        resultado.style.color = "red";
        entradaInput.value = "";
    }
}
