#pintas que hay en ml

ml= float(input('Ingrese el valor en mililitros: '))

def ml_a_pintas(ml):
    return ml/473.176

print ('el valor en pintas de ',ml, ' mililitros es: ',ml_a_pintas(ml)  )