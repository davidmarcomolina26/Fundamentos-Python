#cambio de hora formato 24h a 12h

hora= int(input('Introduzca la hora en formato 24h (0-23): '))
minuto= int(input('Introduzca los minutos (0-59): '))

def paso_a_formato12h(hora,minuto):
    
    if hora > 12:
        hora_final= hora - 12
        periodo= 'PM'
    else:
        hora_final= hora
        periodo= 'AM'
    return hora_final,':',minuto, periodo

try:
    if hora >= 0 and hora <= 24 and minuto >= 0 and minuto <= 59:
        print('La hora convertida es:', paso_a_formato12h(hora,minuto))
    raise ValueError
except:
    print('Error: Hora o minuto no valido')

