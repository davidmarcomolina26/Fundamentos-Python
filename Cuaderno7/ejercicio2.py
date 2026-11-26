#dados dos números, calcule el producto de forma recursiva. Los números a multiplicar deben ser leídos por teclado.

def producto_recursivo(a, b):
    # Caso base: si b es 0, el producto es 0
    if b == 0:
        return 0
    # Si b es negativo, convertimos el problema a positivo
    if b < 0:
        return -producto_recursivo(a, -b)
    # Llamada recursiva: a + producto de a y (b-1)
    return a + producto_recursivo(a, b - 1)

# Lectura de números por teclado
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultado = producto_recursivo(num1, num2)
print(f"El producto de {num1} y {num2} es: {resultado}")