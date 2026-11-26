def leer_validado_entero():
    while True:
        entrada = input("Por favor, ingrese un número entero: ")
     
        try:
           
            numero = int(entrada)
            
            return numero
    
        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar un número entero.")
            

print(leer_validado_entero())