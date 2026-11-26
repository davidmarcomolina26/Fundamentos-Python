#segundos desde medianoche y hasta la siguiente

horas = int(input("Ingrese las horas (0-23): "))
minutos = int(input("Ingrese los minutos (0-59): "))
segundos = int(input("Ingrese los segundos (0-59): "))

total_segundos = horas*3600 + minutos*60 + segundos

desde_medianoche = total_segundos
hasta_siguiente_medianoche = (24*3600) - total_segundos

print("Segundos desde la medianoche:", desde_medianoche)
print("Segundos hasta la siguiente medianoche:", hasta_siguiente_medianoche)