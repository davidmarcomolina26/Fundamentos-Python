a=float(input('Introduce el primer numero: '))
b=float(input('Introduce el segundo numero: '))
c=float(input('Introduce el tercer numero: '))

#funcion segundo grado ax^2+bx+c=0
def solucion_ecuacion(a,b,c):
    discriminante= b**2 -4*a*c
    if discriminante == 0:
        return -b/2*a
    elif discriminante > 0:
        raiz1= (-b + discriminante**0.5)/(2*a)
        raiz2= (-b - discriminante**0.5)/(2*a)
        return raiz1, raiz2
    else:
        return 'No tiene solucion en los reales'
    
try:
    if a==float(a) and b==float(b) and c==float(c):
        print ('la solucion correcta para nuestros datos sera: ', solucion_ecuacion(a,b,c))
    else:
        raise ValueError
except:
    print ('Te has equivocado en las entradas')