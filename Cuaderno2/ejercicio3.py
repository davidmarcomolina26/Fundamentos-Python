#Calculo de TIEA

def TIEA (TNA, m):
    return (1 + TNA / m) ** (m - 1)

TNA=float(input('Ingrese el valor de la TNA en decimal: '))
m=int(input('Ingrese el numero de periodos de capitalizacion por año: '))

print ('El valor del TIEA es', TIEA (TNA,m))