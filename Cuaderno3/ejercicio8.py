entrada = int(input('introduzca un valor entero: '))

def asignar_mes (entrada):
    if entrada==1:
        return 'Enero'
    elif entrada == 2:
        return 'Febrero'
    elif entrada == 3:
        return 'Marzo'
    elif entrada == 4:
        return 'Abril'
    elif entrada == 5:
        return 'Mayo'
    elif entrada == 6:
        return 'Junio'
    elif entrada == 7:
        return 'Julio'
    elif entrada == 8:
        return 'Agosto'
    elif entrada == 9:
        return 'Septiembre'
    elif entrada == 10:
        return 'Octubre'
    elif entrada == 11:
        return 'Noviembre'
    elif entrada == 12:
        return 'Diciembre'

    
try: 
    if entrada >= 1 and entrada <= 12:
        print('El mes correspondiente al numero introducido es:', asignar_mes(entrada))
    else:
        raise ValueError 
        
except:
    print('Error: Numero no valido')