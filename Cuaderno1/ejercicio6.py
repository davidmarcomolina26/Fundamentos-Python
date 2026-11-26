#flota de camiones

distancia_recorrida= float(input('Introduzca la distancia recorrida en km:'))
litros_gasoil= float(input('Introduzca los litros de gasoil consumidos:'))
precio_gasoil= float(input('Introduzca el precio del gasoil por litro:'))   
costes_varios= float(input('Introduzca los costes varios (peajes, dietas, etc):'))

km_por_litro= distancia_recorrida/ litros_gasoil
coste_viaje= (litros_gasoil * precio_gasoil) + costes_varios
coste_por_km= coste_viaje/ distancia_recorrida

print  ('El consumo medio es de:', km_por_litro, 'km/litro')
print  ('El coste total del viaje es de:', coste_viaje, 'euros ')
print  ('El coste por km es de:', coste_por_km, 'euros/km')

