def es_entero(cadena):
    for c in cadena:
        if c < '0' or c > '9':  # Si algún carácter no es un número, regreso False
            return False
    return True if cadena else False  # Me aseguro de que no esté vacía la cadena

# Esta función revisa si el número es decimal (tiene un punto)
def es_decimal(cadena):
    return '.' in cadena

# Esta función revisa si la entrada es puro texto (solo letras y espacios)
def es_texto(cadena):
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚñÑ "
    for c in cadena:
        if c not in letras:  # Si hay un carácter que no es letra o espacio, no es texto puro
            return False
    return True

# Este es el ciclo principal del programa
while True:
    entrada = input("Escribe algo: (o 'salir'): ").strip()  # Pido al usuario que escriba algo

    if entrada.lower() == "salir":  # Si escribió "salir", cierro el programa
        print("¡Programa terminado!")
        break
    elif entrada == "":
        print("Entrada vacía")  # Si no escribió nada, aviso
    elif es_decimal(entrada):
        print("Es decimal")  # Si tiene punto decimal, no lo acepto
    elif es_entero(entrada):
        # Si es un número entero válido, lo convierto manualmente a número
        numero = 0
        for c in entrada:
            numero = numero * 10 + (ord(c) - ord('0'))  # Transformo el carácter a número sumando su valor
        print(f"{numero} es un número entero.")
    
    elif es_texto(entrada):
        print("Es texto")  # Si escribió solo texto, no lo acepto
    else:
        print("Error: entrada no válida")  # Para cualquier otra cosa que no encaje