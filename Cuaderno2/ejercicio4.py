#segundos desde la media noche 

horas=int(input('Ingrese la cantidad de horas: '))
minutos=int(input('Ingrese la cantidad de minutos: '))
segundos=int(input('Ingrese la cantidad de segundos: '))

def horas_minutos_a_segundos (horas,minutos,segundos):
    return horas*3600 + minutos*60 + segundos 

print ('El total de segundos desde la media noche es', horas_minutos_a_segundos (horas,minutos,segundos), 'segundos')

