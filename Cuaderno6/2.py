persona1 = {'nombre': "Ana", 'sexo': "F", 'edad': 28}
persona2 = {'nombre': "Luis", 'sexo': "M", 'edad': 34}
persona3 = {'nombre': "María", 'sexo': "F", 'edad': 22}
persona4 = {'nombre': "Carlos", 'sexo': "M", 'edad': 45}
persona5 = {'nombre': "Sofía", 'sexo': "F", 'edad': 30}
persona6 = {'nombre': "Jorge", 'sexo': "M", 'edad': 27}
persona7 = {'nombre': "Lucía", 'sexo': "F", 'edad': 33}
persona8= {'nombre': "Miguel", 'sexo': "M", 'edad': 29}
persona9 = {'nombre': "Elena", 'sexo': "F", 'edad': 26}
persona10 = {'nombre': "Andrés", 'sexo': "M", 'edad': 31}

lista_personas = [persona1, persona2, persona3, persona4, persona5, persona6, persona7, persona8, persona9, persona10]

def mostrar_datos_persona(lista):
    suma_edades_totales = 0
    suma_edades_mujeres=0
    contador_mujeres=0
    suma_edades_hombres=0
    contador_hombres=0
    mujeres_entre_13_y_16=0
    hombres_menores_20=0

    for persona in lista:
        suma_edades_totales += persona['edad']    #sumo todas las edades
        if persona['sexo'] == 'F':          #si es mujer
            contador_mujeres += 1            #cuento la mujer
            suma_edades_mujeres += persona['edad']   #sumo edades de mujeres
            if 13 <= persona['edad']< 16:    #si la mujer está entre 13 y 16 años
                mujeres_entre_13_y_16 += 1   #cuento la mujer
        elif persona['sexo'] == 'M':        #si es hombre
            contador_hombres += 1            #cuento el hombre
            suma_edades_hombres += persona['edad']  #sumo edades de hombres
            if persona['edad']< 20:       #si el hombre es menor de 20 años
                hombres_menores_20 += 1    #cuento el hombre menor de 20

    media_total = suma_edades_totales / len(lista)
    media_edad_mujeres = suma_edades_mujeres / contador_mujeres 
    media_edad_hombres = suma_edades_hombres / contador_hombres

    #devolver todos los participantes:
    for persona in lista:
        print("Nombre:", persona['nombre'], "- Sexo:", persona['sexo'], "- Edad:", persona['edad'])
    print("Media de edad total:", media_total)
    print("Media de edad mujeres:", media_edad_mujeres)
    print("Media de edad hombres:", media_edad_hombres)
    print("Número de mujeres entre 13 y 16 años:", mujeres_entre_13_y_16)
    print("Número de hombres menores de 20 años:", hombres_menores_20)

mostrar_datos_persona(lista_personas)
    
       
    



    
