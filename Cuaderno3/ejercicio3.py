#es entero

entrada= input('Introduzca un valor: ')

def validar_entero(entrada):
    try:
        entrada==int(entrada)
        return True
    except:
        return False

print('¿El valor introducido es un entero?:', validar_entero(entrada)) 
    