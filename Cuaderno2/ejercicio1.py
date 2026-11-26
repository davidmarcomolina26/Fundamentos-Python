#funcion fuerza
masa=float(input('Ingrese el valor de la masa en kg: '))
aceleracion=float(input('Ingrese el valor de la aceleracion en m/s^2: '))

def fuerza (masa, aceleracion):
    return masa * aceleracion

print ('El valor de la fuerza es',fuerza(masa,aceleracion),'Newtons')