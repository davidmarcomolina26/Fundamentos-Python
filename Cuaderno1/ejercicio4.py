#Impuestos a pagar:

ingresos_anuales= float(input('Introduzca sus ingresos anuales:'))
numero_hijos= int(input('introduzca el numero de hijos que tiene:'))

ingreso_imponible= (ingresos_anuales-600)- (numero_hijos* 60) 
impuesto_a_pagar=1/3 * ingreso_imponible

total= ingresos_anuales-impuesto_a_pagar

print('El impuesto a pagar es de:', impuesto_a_pagar)
print('El total de ingresos despues de impuestos es de:', total)
