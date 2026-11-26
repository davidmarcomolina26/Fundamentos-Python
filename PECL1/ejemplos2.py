def es_primo(n):
    # Los números menores que 2 no son primos
    if n < 2:
        return False
    # 2 es el único número primo par
    if n == 2:
        return True
    # Los números pares mayores que 2 no son primos
    if n % 2 == 0:
        return False
    # Se prueba la divisibilidad solo con números impares hasta la raíz cuadrada
    # (n**0.5) + 1 para incluir la raíz cuadrada en la comprobación
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    # Si no se encontró ningún divisor, el número es primo
    return True



contador = 0
salir = False
entrada=int(input('Escribe algo'))

while salir!=True:
    if entrada <=0:
        salir=True
        print (contador)
    elif es_primo(entrada):
        contador+=1
    else:
        contador +=0
    entrada=int(input('Otro numero va'))


    