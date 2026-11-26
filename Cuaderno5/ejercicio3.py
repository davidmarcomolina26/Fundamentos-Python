def separacion_par_impar_orden(lista_original):
    lista_pares_ascendente = []
    lista_impares_descendente = []
    for numero in lista_original:
        if numero % 2 == 0:
            lista_pares_ascendente.append(numero)
            lista_pares_ascendente.sort()
        else:
            lista_impares_descendente.append(numero)
            lista_impares_descendente.sort(reverse=True)
    print("Lista de números pares en orden ascendente:", lista_pares_ascendente)
    print("Lista de números impares en orden descendente:", lista_impares_descendente)

# Ejemplo de uso
lista_ejemplo = [7, 2, 5, 8, 1, 4, 3, 6]
separacion_par_impar_orden(lista_ejemplo)

    