notas_clase=[1,2,3,4,5,6,7,8,9,10]
def convertir_notas(notas):
    notas_alfanumericas=[]
    for i in notas:
        if 10 >= i >= 9:
            notas_alfanumericas.append('A')
        elif 8 <= i < 9:
            notas_alfanumericas.append('B')
        elif 7 <= i < 8:
            notas_alfanumericas.append('C')
        elif 6 <= i < 7:
            notas_alfanumericas.append('D')
        elif 5 <= i < 6:
            notas_alfanumericas.append('E')
        elif 0 <= i < 5:
            notas_alfanumericas.append('F')
        else:
            notas_alfanumericas.append('Nota inválida')
    return("Notas alfanuméricas:", notas_alfanumericas)

print(convertir_notas(notas_clase))
        
    