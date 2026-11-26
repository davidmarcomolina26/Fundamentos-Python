#operaciones con numeros complejos

#Primer numero
a = int(input("Ingrese la parte real del primer numero complejo: "))
b= int(input("Ingrese la parte imaginaria del primer numero complejo: "))
#Segundo numero
c = int(input("Ingrese la parte real del segundo numero complejo: "))
d = int(input("Ingrese la parte imaginaria del segundo numero complejo: "))

print ("El primer numero complejo es:",a,"+",b,"i")
print ("El segundo numero complejo es:",c,"+",d,"i")

#operacion suma:
def suma_complejos (a,b,c,d):
    parte_real = a+b
    parte_imaginaria= (c+d)
    return parte_real,'+',parte_imaginaria,'i'

print("La suma de los numeros complejos es:",suma_complejos(a,b,c,d))

#operacion resta:
def resta_complejos (a,b,c,d):
    parte_real=a-b
    parte_imaginaria=c-d
    return parte_real,'+',parte_imaginaria,'i'

print("La resta de los numeros complejos es:",resta_complejos(a,b,c,d))

#operacion producto:
def producto_complejos (a,b,c,d):
    parte_real= (a*c)-(b*d)
    parte_imagnaria= (a*d)+(b*c)
    return parte_real,'+',parte_imagnaria,'i'
print("El producto de los numeros complejos es:",producto_complejos(a,b,c,d))

#operacion division:
def division_complejos (a,b,c,d):
    parte_real= ((a*c)+(b*d))/((c**2)+(d**2))
    parte_imaginaria= ((b*c)-(a*d))/((c**2)+(d**2))
    return parte_real,'+',parte_imaginaria,'i'
print("La division de los numeros complejos es:",division_complejos(a,b,c,d))


