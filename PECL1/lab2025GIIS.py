#Parte1
def longitud_secuencia(cadena):
    contador=0
    for i in cadena:
        contador+=1
    return contador

#Parte2
import random

def menor_longitud_frases(frase1,frase2):
    if frase1<=frase2:
        return frase1
    else:
        return frase2
    
n=random.randint(3,10)
print('se van a imprimir',n,'frases')
frase_base=input('Dame una frase base: ')
menor=frase_base
for i in range (2,n+1):
    print('llevas',i,'frases')
    frase_nueva=input('Dame una frase nueva ')
    menor=menor_longitud_frases(frase_base,frase_nueva)
    print (menor)
print('La frase menor es',menor)
