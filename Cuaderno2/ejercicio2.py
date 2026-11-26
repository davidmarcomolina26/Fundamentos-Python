#Funcion de barn a metro cuadrado y inversa

def barn_a_metro_cuadrado(barn):
    return barn * 1e-28

def metro_cuadrado_a_barn(metro_cuadrado):
    return metro_cuadrado / 1e-28

barn = float(input('Ingrese el valor en barn: '))
metro_cuadrado = float(input('Ingrese el valor en metro cuadrado: '))

print(f'{barn} barn son {barn_a_metro_cuadrado(barn)} metros cuadrados')
print(f'{metro_cuadrado} metros cuadrados son {metro_cuadrado_a_barn(metro_cuadrado)} barn')

