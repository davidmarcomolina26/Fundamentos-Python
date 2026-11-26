
anio=int(input('Introduzca un año entero: '))

def es_bisiesto (anio):
    if anio < 1582:
        return 'No se puede determinar si es bisiesto o no'
    else:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            return True
        else:
            return False
        
try:
    if anio==int(anio):
        print('¿El año introducido es bisiesto?:', es_bisiesto(anio))
    else:
        raise ValueError
    
except:
    print ('error en la entrada de datos')