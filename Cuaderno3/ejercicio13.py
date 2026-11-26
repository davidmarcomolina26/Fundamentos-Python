kilometros= float(input('introduzca los kilometros recorridos: '))

def coste_total (kilometros):
    cuota_base=100
    
    if kilometros <= 300:
        return cuota_base 
    elif 300 < kilometros <= 1000:
        excedente=(kilometros-300)*0.30
        return cuota_base+excedente
    elif kilometros>1000:
        excedente1=(1000-300)*0.30
        excedente2=(kilometros-1000)*0.20
        return cuota_base+excedente1+excedente2
    else:
        return 'error'
    
print('el coste total del alquiler es de: ', coste_total(kilometros), 'euros')


       