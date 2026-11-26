#es bisisiesto??? sin ifs

anio=int(input('Introduzca el año que desee comprobar:  '))

def es_bisiesto(anio):
    comprobacion1= anio % 4 == 0 and anio % 100 != 0
    comprobacion2= anio % 400 == 0
    return comprobacion1 or comprobacion2
print('¿El año',anio,'es bisiesto?:',es_bisiesto(anio))