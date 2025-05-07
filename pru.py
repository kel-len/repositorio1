# Esta función me dice si un número es primo o no
def primos(n):
    if n < 2:  # Si el número es menor que 2, no es primo
        return False
    # Recorro desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:  # Si el número se divide exacto por otro, no es primo
            return False
    return True  # Si no se dividió por ningún otro, sí es primo

# Esta función revisa si una cadena es un número entero (solo contiene dígitos)
def es_entero(cadena):
    for c in cadena:
        if c < '0' or c > '9':  # Si algún carácter no es un número, regreso False
            return False
    return True if cadena else False  # Me aseguro de que no esté vacía la cadena

# Esta función revisa si el número es decimal (tiene un punto)
def es_decimal(cadena):
    return '.' in cadena

# Esta función revisa si el número es negativo (empieza con '-')
def es_negativo(cadena):
    return cadena[0] == '-' if cadena else False  # Si la cadena no está vacía y empieza con '-', es negativo

# Esta función revisa si la entrada es puro texto (solo letras y espacios)
def es_texto(cadena):
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚñÑ "
    for c in cadena:
        if c not in letras:  # Si hay un carácter que no es letra o espacio, no es texto puro
            return False
    return True

# Esta función busca si hay caracteres no permitidos como símbolos raros
def caracteres_invalidos(cadena):
    permitidos = "0123456789.-"  # Solo permito números, punto y guion
    for c in cadena:
        if c not in permitidos:  # Si hay algo fuera de esto, regreso True
            return True
    return False

# Este es el ciclo principal del programa
while True:
    entrada = input("Ingresa un número entero positivo (o 'salir'): ").strip()  # Pido al usuario que escriba algo

    if entrada.lower() == "salir":  # Si escribió "salir", cierro el programa
        print("¡Programa terminado!")
        break
    elif entrada == "":
        print("Entrada vacía")  # Si no escribió nada, aviso
    elif es_negativo(entrada):
        print("Error: número negativo")  # Si es un número negativo, no lo acepto
    elif es_decimal(entrada):
        print("Error: número decimal")  # Si tiene punto decimal, no lo acepto
    elif es_entero(entrada):
        # Si es un número entero válido, lo convierto manualmente a número
        numero = 0
        for c in entrada:
            numero = numero * 10 + (ord(c) - ord('0'))  # Transformo el carácter a número sumando su valor
        print(f"{numero} es un número entero.")
        if primos(numero):  # Llamo a la función para ver si es primo
            print(f"{numero} es PRIMO.")
        else:
            print(f"{numero} NO es primo.")
    elif es_texto(entrada):
        print("Error: texto no permitido")  # Si escribió solo texto, no lo acepto
    elif caracteres_invalidos(entrada):
        print("Error: contiene caracteres especiales")  # Si hay símbolos raros, muestro error
    else:
        print("Error: entrada no válida")  # Para cualquier otra cosa que no encaje
