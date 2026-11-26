#Vocal o no

#Input del programa
letra= (input('Introduzca una letra:  '))

#funcion para determinar si es vocal o no
def es_vocal(letra):
    if letra == 'A':
        return True
    elif letra == 'E':
        return True
    elif letra == 'I':
        return True
    elif letra == 'O':
        return True
    elif letra == 'U':
        return True
    else:
        return False
    
try:
    if letra == str(letra):
        print('¿La letra introducida es una vocal?:', es_vocal(letra.upper()))
    
except:
    print('Error: no es una letra valida')
