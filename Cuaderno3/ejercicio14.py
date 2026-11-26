ingreso= float(input('introduzca su ingreso familiar para darle los puntos: '))

def puntos(ingreso):
    if 0<ingreso<1800:
        return 'ha conseguido 4 puntos'
    elif 1800<=ingreso<3500:
        return 'ha conseguido 3 puntos'
    elif 3500<= ingreso < 5000:
        return 'ha conseguido 2 puntos'
    elif ingreso >=5000:
        return 'ha conseguido 1 punto'
    else:
        return 'ingreso no valido'

print(puntos(ingreso))    