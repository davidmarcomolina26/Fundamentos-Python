#funciones de areas:

#area de un circulo:
import math

def area_circulo (radio):
    area= math.pi * (radio**2)
    return area

#area de un cuadrado:
def area_cuadrado (lado):
    area= lado**2
    return area

#area de un trianngulo:
def area_triangulo (base, altura):
    area= (base*altura)/2
    return area