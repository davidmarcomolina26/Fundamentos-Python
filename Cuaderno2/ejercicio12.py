#nota con varios decimales a nota con un decimal solo usando funciones

nota=float(input('Introduzca la nota que ha obtenido: '))

#posibilidad de salida es X.0 o X.5

def conversion_nota(nota):
    parte_entera= int(nota)
    parte_decimal= nota - parte_entera
    

    
