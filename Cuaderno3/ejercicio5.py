#Nota de clase

#Input del programa
nota= (input('Introduzca la nota obtenida en forma numerica: '))

#funcion para convertir la nota a valor numerico

def cambio_numerico (nota):
    if nota >= 8.5 and nota <= 10:
        return 'A'
    elif nota >= 6.5 and nota < 8.5:
        return 'B'
    elif nota >= 5 and nota < 6.5:
        return 'C'
    elif nota >= 3.5 and nota < 5:
        return 'D'
    elif nota < 3.5 and nota >= 0:
        return 'F'
    
try:
    if nota>=0 and nota <=10:
        print('La nota en formato alfabetico es:', cambio_numerico(nota))
    
except:
    print('Error: no es una nota valida')

