def es_multiplo3(num):
    if num%3==0:
        valor = True
    else:
        valor = False
    return valor


def es_multiplo5(num):
    if num%5==0:
        valor= True
    else:
        valor= False
    return valor

def fizzbuzz (min,max):
    for i in range(min, max+1):
        if es_multiplo3(i) and es_multiplo5(i):
            print ('fizzbuzz')
        elif es_multiplo3(i):
            print ('fizz')
        elif es_multiplo5(i):
            print ('buzz')
        else:
            print(i)
    print()
    return ''
print (fizzbuzz(1,100))