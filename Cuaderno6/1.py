#se deberá almacenar el nombre, sexo y edad de cada persona
#rograma posteriormente una función para leer por teclado datos relativos a una persona y otra que muestra dichos datos por pantalla

def leer_datos_persona():
    nombre = input("Ingrese el nombre de la persona: ")
    sexo = input("Ingrese el sexo de la persona (M/F): ")
    edad = int(input("Ingrese la edad de la persona: "))
    return {'nombre': nombre, 'sexo': sexo, 'edad': edad}

def mostrar_datos_persona(persona):
    print("Datos de la persona:")
    print("Nombre:", persona['nombre'])
    print("Sexo:", persona['sexo'])
    print("Edad:", persona['edad'])

# Ejemplo de uso
persona = leer_datos_persona()
mostrar_datos_persona(persona)
