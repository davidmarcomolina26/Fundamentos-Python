#Salario Neto
total_ventas=int(input('introduzca el total de ventas realizadas:  '))

salario_fijo=2000
suma_total= salario_fijo + (total_ventas * 0.03)

salario_neto= suma_total - (suma_total * 0.32)

print('El salario neto es de:', salario_neto, 'euros')
