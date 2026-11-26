#Primera Funcion: imprimir_tablero
def imprimir_tablero(n, jx,jy, mx,my):
    for i in range (n):
        for j in range(n):
            if i==jy and j==jx:
                print("X", end=" ")
            elif i==my and j==mx:
                print("O", end=" ")
            else:
                print("#", end=" ")
            print (' ',end='')
        print()
    for guion in range (2*n-1):
        print('-', end='')
    print()

#probador:
imprimir_tablero(5, 0, 1, 3, 4)

#Segunda Funcion: Pedir Movimientos

def pedir_movimientos():
    salir=False
    cadena=input('Introduce una secuencia de movimientos (e/o/n/s: )')

    while salir != True:
        for caracter in cadena:
            if caracter =='e' or caracter =='o' or caracter =='n' or caracter =='s':
                salir = True
                return cadena
            else:
                print('Error: Secuencia no valida')
                cadena=input('Introduce una secuencia de movimientos (e/o/n/s: )')

#probador:
print(pedir_movimientos())

import random

def calcular_recompensa(secuencia):
    recompensa_i=random.randint(10000,15000)
    recompensa_f=recompensa_i
    contador=1
    for i in secuencia:
        if contador%2==0 and contador!=0:
            recompensa_f=recompensa_f//10
            contador+=1
        else:
            contador+=1
    return ('partias de una recompensa',recompensa_i,'y se te ha quedado en', recompensa_f)

#probador
print(calcular_recompensa('n'))
