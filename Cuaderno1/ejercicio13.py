#cambio a libras esterlinas

euros = float(input('Introduzca la cantidad de euros: '))
precio_libra= float(input('introduzca el precio de la libra a dia de hoy: '))

cambio_a_libras= euros * precio_libra
total= cambio_a_libras - (cambio_a_libras*0.02)

print('El total en libras esterlinas es de:', total, 'libras')

