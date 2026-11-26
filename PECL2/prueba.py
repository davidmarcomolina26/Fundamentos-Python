def pinta_lista(lista):
    if len(lista) == 0:
        print (lista)
    else:
        print(lista)
        pinta_lista(lista[:-1])
        print(lista)

# Pruebas  
mi_lista = [1, 2, 3, 4, 5]
pinta_lista(mi_lista)