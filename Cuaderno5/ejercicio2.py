def suma_listas_desiguales(lista1,lista2):
    lista_final=[]
    longitud_maxima = max(len(lista1), len(lista2))
    for i in range(longitud_maxima):
        if i < len(lista1):
            valor1 = lista1[i]
        else:
            valor1 = 0
        if i < len(lista2):
            valor2 = lista2[i]
        else:
            valor2 = 0
        lista_final.append(valor1 + valor2)
    print(lista_final)

# Ejemplo de uso
lista_a = [1, 2, 3, 7]
lista_b = [4, 5, 6]
resultado = suma_listas_desiguales(lista_a, lista_b)