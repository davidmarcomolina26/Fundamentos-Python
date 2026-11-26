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
ruta_reparto = {"Rovaniemi-Alcalá de Henares": 150,
"Alcalá de Henares-Marchamalo": 80,
"Marchamalo-Guadalajara": 15,
"Guadalajara-Zaragoza": 250,
"Zaragoza-Pamplona": 180,
"Pamplona-Vitoria": 120,
"Vitoria-Bilbao": 70,
"Bilbao-Santander": 100,
"Santander-León": 200,
"León-Salamanca": 180}

def reno_joven_reno_viejo(renos):
    joven=' '
    viejo=' '
    for reno in renos:
        if joven == ' ' or reno['edad'] < joven['edad']:
            joven = reno
        if viejo == ' ' or reno['edad'] > viejo['edad']:
            viejo = reno
    
    print ("Reno más joven:", joven['nombre'], "Edad:", joven['edad'])
    print ("Reno más viejo:", viejo['nombre'], "Edad:", viejo['edad'])
    return ' '

print(reno_joven_reno_viejo(renos_papa_noel))