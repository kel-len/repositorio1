def es_entero(cadena): 
    for c in cadena:
        if c < '0' or c > '9':
            return False
    return True if cadena else False

def es_decimal(cadena):
    return '.' in cadena

def es_texto(cadena):
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚñÑ "
    for c in cadena:
        if c not in letras:
            return False
    return True

while True:
    entrada = input("Escribe algo: (o 'salir'): ").strip()

    if entrada.lower() == "salir":
        print("¡Programa terminado!")
        break
    elif entrada == "":
        print("Entrada vacía")
    elif es_decimal(entrada):
        print("Es decimal")
    elif es_entero(entrada):
        numero = 0
        for c in entrada:
            numero = numero * 10 + (ord(c) - ord('0'))
        print(f"{numero} es un número entero.")
    elif es_texto(entrada):
        print("Es texto")
    else:
        print("Error: entrada no válida")
