renos_papa_noel = [
{"nombre": "Blitzen", "edad": 7, "velocidad_media": 17, "distancia_maxima": 93},
{"nombre": "Comet", "edad": 5, "velocidad_media": 21, "distancia_maxima": 98},
{"nombre": "Cupid", "edad": 6, "velocidad_media": 19, "distancia_maxima": 92},
{"nombre": "Dancer", "edad": 6, "velocidad_media": 18, "distancia_maxima": 95},
{"nombre": "Dasher", "edad": 5, "velocidad_media": 20, "distancia_maxima": 100},
{"nombre": "Donner", "edad": 4, "velocidad_media": 23, "distancia_maxima": 107},
{"nombre": "Olive", "edad": 8, "velocidad_media": 15, "distancia_maxima": 85},
{"nombre": "Prancer", "edad": 4, "velocidad_media": 22, "distancia_maxima": 105},
{"nombre": "Rudolph", "edad": 3, "velocidad_media": 25, "distancia_maxima": 110},
{"nombre": "Vixen", "edad": 7, "velocidad_media": 16, "distancia_maxima": 90}]

def reno_mas_joven(renos):
    joven= None
    for reno in renos:
        if joven == None or reno['edad']< joven['edad']:
            joven= reno
    return joven['nombre']
print(reno_mas_joven(renos_papa_noel))

#Calcular tiempo dado un reno y una distancia teniendo en cuenta que cada distancia maxima se hace una parada de 30 min

def tiempo_renos(reno, distancia):
    distancia_maxima=reno['distancia_maxima']
    velocidad_media=reno['velocidad_media']
    tiempo_total=0
    contador_distancia=0
    while contador_distancia < distancia:
        if distancia - contador_distancia <= distancia_maxima:
            tiempo_total += (distancia - contador_distancia) / velocidad_media
            contador_distancia = distancia
        else:
            tiempo_total += distancia_maxima / velocidad_media
            tiempo_total += 0.5  # parada de 30 min
            contador_distancia += distancia_maxima
    return tiempo_total

print(tiempo_renos(renos_papa_noel[8], 250))  # Ejemplo con Rudolph y 250 km
