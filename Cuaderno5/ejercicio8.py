#dos cadenas de caracteres son iguales, sin comparar las cadenas completas y sin usar el operador in.
def comparar_cadenas(cadena1,cadena2):
    if len(cadena1) != len(cadena2):
        return False
    
    else:
        pos=0
        while pos < len(cadena1):
            if cadena1[pos] != cadena2[pos]:
                return False
            pos += 1
    return True

# Ejemplo de uso
cadena_a = "hola mundo"
cadena_b = "hola mundo"
print(comparar_cadenas(cadena_a, cadena_b))

