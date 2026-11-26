#a partir de coordenadas 3d calcular la distancia entre dos puntos

import math

x1=float(input('Ingrese la coordenada x1: '))
y1=float(input('Ingrese la coordenada y1: '))
z1=float(input('Ingrese la coordenada z1: '))
x2=float(input('Ingrese la coordenada x2: '))
y2=float(input('Ingrese la coordenada y2: '))
z2=float(input('Ingrese la coordenada z2: '))
def distancia_3d(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

print('La distancia entre los dos puntos es', distancia_3d(x1, y1, z1, x2, y2, z2))