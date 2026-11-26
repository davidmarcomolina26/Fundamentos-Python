#Importe de venta

importe= float(input('Introduzca el importe de la venta: '))
forma_pago= int(input('Introduzca la forma de pago (0-efectivo, 1-tarjeta: '))

#funcion para calcular el importe final:
def importe_final(importe,forma_pago):
    if importe > 100:
        if forma_pago == 0:
            descuento= importe*0.05
        elif forma_pago == 1:
            descuento= importe*0.02
        else:
            print('Error: Forma de pago no valida')
    else:
        descuento= 0
    importe_con_descuento= importe - descuento
    return importe_con_descuento

#Comprobamos lo primero de todo la entrada de datos
try:
    if importe > 0 and forma_pago == 0 or forma_pago == 1:
        print ('El importe final es de:', importe_final(importe,forma_pago))
        raise ValueError
except:
    print('Error: Forma de pago no valida')


    
   





