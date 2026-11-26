#palabra contiene las cinco vocales
def contiene_vocales(palabra):
    vocales= 'aeiou'
    for vocal in vocales:
        if vocal not in palabra.lower():
            return False
    return True

# Ejemplo de uso
palabra_ejemplo = "Educacion"
palabra_ejemplo2 = 'llll'
print(contiene_vocales(palabra_ejemplo2))