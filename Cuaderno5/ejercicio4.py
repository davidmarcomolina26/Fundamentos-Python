#generamos lista de enteros aleatorios
import random
def generar_lista_aleatoria(longitud_lista):
    rango_minimo=1
    rango_maximo=20
    lista_aleatoria=[]
    for num in range(longitud_lista):
        numero_aleatorio=random.randint(rango_minimo,rango_maximo)
        lista_aleatoria.append(numero_aleatorio)
    
    valor_mas_alto=max(lista_aleatoria)
    valor_mas_bajo=min(lista_aleatoria)
    media=sum(lista_aleatoria)/len(lista_aleatoria)

    print("Lista aleatoria generada:", lista_aleatoria)
    print("Valor más alto:", valor_mas_alto)
    print("Valor más bajo:", valor_mas_bajo)
    print("Media de los valores:", media)


# Ejemplo de uso
longitud=int(input("Ingrese la longitud de la lista aleatoria: "))
generar_lista_aleatoria(longitud)
