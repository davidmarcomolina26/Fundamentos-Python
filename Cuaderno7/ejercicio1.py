def esta_en_lista_recursiva(lista, elemento):
    # Caso base: si la lista está vacía, el elemento no está presente
    if not lista:
        return False
    # Si el primer elemento es el que buscamos, devolvemos True
    if lista[0] == elemento:
        return True
    # Llamada recursiva con el resto de la lista
    return esta_en_lista_recursiva(lista[1:], elemento)

# Pruebas
mi_lista = [1, 2, 3, 4, 5]

print(esta_en_lista_recursiva(mi_lista, 3))  # Debería devolver True
print(esta_en_lista_recursiva(mi_lista, 6))  # Debería devolver False