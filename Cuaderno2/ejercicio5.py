#punto en 2D esta o no en el circulo
x=float(input('Ingrese la coordenada x del punto: '))
y=float(input('Ingrese la coordenada y del punto: '))

def esta_en_circulo(x,y):
    return x**2+y**2<=1000

print ('El punto (',x,',',y,') esta dentro del circulo de radio 10?', esta_en_circulo(x,y))

