#orden de 3 enteros

#Input del programa
a= (input('Introduzca el primer numero entero: '))
b= (input('Introduzca el segundo numero entero: '))
c= (input('Introduzca el tercer numero entero: '))

#funcion
def orden_creciente(a,b,c):
    if a>=b>=c:
        return a,b,c
    elif a>=c>=b:
        return a,c,b
    elif b>=a>=c:
        return b,a,c
    elif b>=c>=a:
        return b,c,a
    elif c>=a>=b:
        return c,a,b
    elif c>=b>=a:
        return c,b,a
    else:
        return 'Error'
    
try:
    if a == int (a) and b ==int(b) and c==int(c):
        print('Los numeros ordenados de mayor a menor son:', orden_creciente(a,b,c))
    
except:
    print('Error: no es un numero entero valido')