def suma_listas(lista1, lista2):
    if len(lista1) != len(lista2):
        return "Error: Las listas deben tener la misma longitud."
    lista_final=[]
    for i in range(len(lista1)):
        lista_final.append(lista1[i] + lista2[i])
    print(lista_final)

# Ejemplo de uso
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
resultado = suma_listas(lista_a, lista_b)
