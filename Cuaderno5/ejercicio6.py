def es_palindromo(lista):
    if lista == lista[::-1]:
        print("La lista es un palíndromo.")
    else:
        print("La lista no es un palíndromo.")
# Ejemplo de uso
lista_ejemplo = [1, 2, 3, 2, 1]
es_palindromo(lista_ejemplo)
