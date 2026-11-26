#de grados a farenheit y kelvin 

grados = float(input('Ingrese el valor en grados Centigrados:  '))
def grados_a_farenheit(grados):
    return (9*grados)/5 + 32

def grados_a_kelvin(grados):
    return grados + 273.15

print (grados, 'grados centrigrados, corresponden a', grados_a_farenheit(grados), 
       'grados Farenheit y a', grados_a_kelvin(grados), 'grados Kelvin'  )