def frase_mayus(frase):
    resultado=''
    nueva_palabra=True

    for caracter in frase:
        if caracter == ' ':
            resultado += caracter
            nueva_palabra = True
        else:
            if nueva_palabra:
                resultado += caracter.upper()
                nueva_palabra = False
            else:
                resultado += caracter.lower()
    return resultado

# Ejemplo de uso
frase_ejemplo = "hOlA mUnDo eStO eS uN pRObLEma"
frase_convertida = frase_mayus(frase_ejemplo)
print(frase_convertida)
