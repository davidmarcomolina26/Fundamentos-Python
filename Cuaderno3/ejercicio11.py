import math

angulo=float(input('introduzca el angulo que desee comprobar'))

opcion= int(input('elija una opcion para comprobar su angulo:'\
'\n 1.Seno\n 2.Coseno\n 3.Tangente\n 4.Cotangente\n 5.Secante\n 6.Cosecante\n'))

def resultado_opcion (opcion,angulo):
    if opcion==1:
        return math.sin(angulo)
    elif opcion==2:
        return math.cos(angulo)
    elif opcion==3:
        return math.tan(angulo)
    elif opcion==4:
        return math.cos(angulo) / math.sin(angulo)
    elif opcion==5:
        return 1/math.cos(angulo)
    elif opcion==6:
        return 1/math.sin(angulo)
    else:
        print ('no es valido ese numero para nuestras opciones')

print ('la opcion elegida ha sido',opcion,'y su resultado es: ',resultado_opcion(opcion,angulo))